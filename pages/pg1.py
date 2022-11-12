import dash
from dash import dcc, html, callback, Output, Input
import dash_bootstrap_components as dbc


dash.register_page(__name__, path='/', name='Introduction') # '/' is home page



layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.Div("What is phishing website?",style={'fontSize':28, "margin-left":"280px","margin-top": "70px","color": "white"} ))                                
    ]),

    dbc.Row([
        dbc.Col(html.Div("So various clients buy items on the web and make installments through different sites. Numerous sites request that the client give touchy information, for example, username, password or credit card or bank details, etc. often for malicious reasons. .",style={'fontSize':17,"margin-top": "34px","margin-left": "30px","margin-right": "70px","color": "white",'textAlign':'justify',} ))                                
    ]),
    dbc.Row([
        dbc.Col(html.Div("This sort of site is known as a phishing website. To distinguish and anticipate a phishing site, we proposed a savvy, adaptable and successful framework that depends on ML. We implemented some algorithms and techniques to extract the phishing data for setting the criteria to classify their legitimacy. The phishing site can be recognized dependent on some significant qualities like URL and Domain Identity, and security and encryption criteria in the last phishing location rate.",style={'fontSize':17,"margin-top": "30px","margin-left": "30px","margin-right": "70px","color": "white",'textAlign':'justify',} ))                                
    ]),
    dbc.Row([
        dbc.Col(html.Div("With the assistance of this framework, the client can likewise buy items online decisively. The administrator can include phishing site URL or phony site URL into a framework where the framework could access and sweep the phishing site and by utilizing the calculation, it will add new suspicious watchwords to the database. The framework utilizes ML innovation to add new watchwords to the database.",style={'fontSize':17,"margin-top": "30px","margin-left": "30px","margin-right": "70px","color": "white",'textAlign':'justify',} ))                                
    ]),

    dbc.Row([
        dbc.Col(html.Div("Let’s look at this URL: signin.eby.de.zukruygxctzmmqi.civpro.co.za",style={'fontSize':24,"margin-top": "50px","margin-left": "30px","margin-right": "50px","color": "white",'textAlign':'justify',} ))                                
    ]),
    dbc.Row([
        dbc.Col(html.Div("So here we are going to have two main techniques, the first one is hexadecimal encoding, in this case, the URL above is going to redirect us to intezer.com since that is the hexadecimal value I inserted above. How about the first part which led you to believe this was actually google.com?Well, some websites allow you to log in by setting passwords and usernames inside the URL itself. If the website does not allow this it has no effect.",style={'fontSize':17,"margin-top": "20px","margin-left": "30px","margin-right": "70px","color": "white",'textAlign':'justify',} ))                                
    ]),
    dbc.Row([
        dbc.Col(html.Div("Actual website – intezer.com (written in hexadecimal)",style={'fontSize':17,"margin-top": "20px","margin-left": "30px","margin-right": "50px","color": "white",'textAlign':'justify',} ))                                
    ]),



])


