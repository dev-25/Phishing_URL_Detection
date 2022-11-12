import dash
from dash import dcc, html, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

import re
import numpy as np
import pandas as pd
from sklearn import tree

from colorama import Fore

from urllib.parse import urlparse

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import GaussianNB
from tld import get_tld, is_tld

dash.register_page(__name__, name='Detection')

data = pd.read_csv('malicious_phish.csv')
data2=data.copy()

# deleting the defacements
indexNames = data2[ data2['type'] == 'defacement' ].index
# Delete these row indexes from dataFrame
data2.drop(indexNames , inplace=True)

# deleting the malwares
indexNames = data2[ data2['type'] == 'malware' ].index
# Delete these row indexes from dataFrame
data2.drop(indexNames , inplace=True)

data2['url'] = data2['url'].replace('www.', '', regex=True)
rem = {"Category": {"benign": 0,  "phishing":1}}
data2['Category'] = data2['type']
data2 = data2.replace(rem)

data2['url_len'] = data2['url'].apply(lambda x: len(str(x)))

def process_tld(url):
    try:
        res = get_tld(url, as_object = True, fail_silently=False,fix_protocol=True)
        pri_domain= res.parsed_url.netloc
    except :
        pri_domain= None
    return pri_domain

data2['domain'] = data2['url'].apply(lambda i: process_tld(i))

feature = ['@','?','-','=','.','#','%','+','$','!','*',',','//']
for a in feature:
    data2[a] = data2['url'].apply(lambda i: i.count(a))

def abnormal_url(url):
    hostname = urlparse(url).hostname
    hostname = str(hostname)
    match = re.search(hostname, url)
    if match:
        return 1
    else:
        return 0
        
data2['abnormal_url'] = data2['url'].apply(lambda i: abnormal_url(i))

def httpSecure(url):
    htp = urlparse(url).scheme #It supports the following URL schemes: file , ftp , gopher , hdl , 
                               #http , https ... from urllib.parse
    match = str(htp)
    if match=='https':
        return 1
    else:
        return 0
data2['https'] = data2['url'].apply(lambda i: httpSecure(i))


def digit_count(url):
    digits = 0
    for i in url:
        if i.isnumeric():
            digits = digits + 1
    return digits
data2['digits']= data2['url'].apply(lambda i: digit_count(i))


def letter_count(url):
    letters = 0
    for i in url:
        if i.isalpha():
            letters = letters + 1
    return letters

data2['letters']= data2['url'].apply(lambda i: letter_count(i))


def Shortining_Service(url):
    match = re.search('bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|'
                      'yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|'
                      'short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|'
                      'doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|'
                      'db\.tt|qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|'
                      'q\.gs|is\.gd|po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|'
                      'x\.co|prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|'
                      'tr\.im|link\.zip\.net',
                      url)
    if match:
        return 1
    else:
        return 0
    
data2['Shortining_Service'] = data2['url'].apply(lambda x: Shortining_Service(x))


def having_ip_address(url):
    match = re.search(
        '(([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.'
        '([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\/)|'  # IPv4
        '(([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.'
        '([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\/)|'  # IPv4 with port
        '((0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\/)' # IPv4 in hexadecimal
        '(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}|'
        '([0-9]+(?:\.[0-9]+){3}:[0-9]+)|'
        '((?:(?:\d|[01]?\d\d|2[0-4]\d|25[0-5])\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d|\d)(?:\/\d{1,2})?)', url)  # Ipv6
    if match:
        return 1
    else:
        return 0
data2['having_ip_address'] = data2['url'].apply(lambda i: having_ip_address(i))


X = data2.drop(['url','type','Category','domain'],axis=1)#,'type_code'
y = data2['Category']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)

from sklearn.metrics import plot_confusion_matrix
from sklearn.metrics import plot_roc_curve
models = [DecisionTreeClassifier,RandomForestClassifier,SGDClassifier]
# models = [DecisionTreeClassifier,RandomForestClassifier,SGDClassifier]
accuracy_test=[]
for m in models:
    model_ = m()
    model_.fit(X_train, y_train)
    pred = model_.predict(X_test)
    acc = accuracy_score(pred, y_test)
    accuracy_test.append(acc)
 
    cf_matrix = confusion_matrix(y_test, pred)

def URL_Converter(urls):
    data= pd.DataFrame()
    data['url'] = pd.Series(urls)

    
    data['url_len'] = data['url'].apply(lambda x: len(str(x)))
    data['domain'] = data['url'].apply(lambda i: process_tld(i))
    feature = ['@','?','-','=','.','#','%','+','$','!','*',',','//']
    for a in feature:
        data[a] = data['url'].apply(lambda i: i.count(a))  
    data['abnormal_url'] = data['url'].apply(lambda i: abnormal_url(i))
    data['https'] = data['url'].apply(lambda i: httpSecure(i))
    data['digits']= data['url'].apply(lambda i: digit_count(i))
    data['letters']= data['url'].apply(lambda i: letter_count(i))
    data['Shortining_Service'] = data['url'].apply(lambda x: Shortining_Service(x))
    data['having_ip_address'] = data['url'].apply(lambda i: having_ip_address(i))
    print(data.columns)
    X = data.drop(['url','domain'],axis=1)
    
    return X

def fnc(test_data):
    models22 = [DecisionTreeClassifier]
    for mm in models22:
        model_ = mm()
        model_.fit(X_train, y_train)
        pred1 = model_.predict(test_data)

    models11 = [RandomForestClassifier]
    for mh in models11:
        model_ = mh()
        model_.fit(X_train, y_train)
        pred2 = model_.predict(test_data)

    models33 = [SGDClassifier]
    for md in models33:
        model_ = md()
        model_.fit(X_train, y_train)
        pred3 = model_.predict(test_data)

    # if pred1[0] == 1:
    if pred1[0] == pred2[0] == pred3[0] == 1:
        return "The Above Link is NOT Valid and is a Phishing Site"
    else:
        return "The Above Link is Valid"

layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.Div("Please enter a URL..",style={'fontSize':28, "margin-left":"140px","margin-top": "70px","color": "white"} ))                                
    ]),

    dbc.Row([
        dbc.Textarea(id='input',className="mb-3", size="lg",style={'fontSize':17,"margin-top": "15px","margin-left":"150px",'border-color':'#303841',"height":"30px","borderRadius": "10px", 'background-color':'#966fd6',"color": "white","width":"750px"},placeholder="URL..."),
                        ]
   ,style={"boxshadow": "greenyellow"}),

    dbc.Button('Submit', id='button1', n_clicks=0,style={'background-color':'#653780', "margin-left":"140px","borderRadius": "5px"}),
    
    dbc.Row([
            dbc.Col(html.Div(id="output",style={"margin-top": "70px",'fontSize':17,"margin-left": "140px","color": "white"}),)                                
        ]),

    dbc.Row([
            dbc.Col(html.Div(".",style={'fontSize':2, "margin-left":"140px","margin-top": "380px","color": "white"} ))                                
    ]),
])         
# ], fluid=True,style={'backgroundColor':'#000000'})

@callback(Output('output', 'children'),
    Input('button1', 'n_clicks'),
    State('input', 'value')
)
def update_output(n_clicks, value):
    if n_clicks > 0:
        
        test_data = URL_Converter(value)
        aaa = fnc(test_data)
        return aaa