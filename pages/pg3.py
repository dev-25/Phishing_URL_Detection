import dash
from dash import dcc, html
from dash import dcc, html, callback, Output, Input
import dash_bootstrap_components as dbc
dash.register_page(__name__, name='Algorithm')

layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.Div("Algorithm used in our project !!",style={'fontSize':28, "margin-left":"260px","margin-top": "70px","color": "white"} ))                                
    ]),

    dbc.Row([
        dbc.Col(html.Div("1. DecisionTreeClassifier",style={'fontSize':22,"margin-top": "30px","margin-left": "30px","margin-right": "50px","color": "white",'textAlign':'justify',} ))                                
    ]),
    dbc.Row([
        dbc.Col(html.Div("Decision Tree is a Supervised Machine Learning Algorithm that uses a set of rules to make decisions, similarly to how humans make decisions. One way to think of a Machine Learning classification algorithm is that it is built to make decisions. You usually say the model predicts the class of the new, never-seen-before input but, behind the scenes, the algorithm has to decide which class to assign. Some classification algorithms are probabilistic, like Naive Bayes, but there’s also a rule-based approach.We humans, also make rule-based decisions all the time.When you’re planning your next vacation, you use a rule-based approach. You might pick a different destination based on how long you’re going to be on vacation, the budget available or if your extended family is coming along.The answer to these questions informs the final decision. And if you continually narrow down the available vacation destinations based on how you answer each question, you can visualize this decision process as a (decision) tree.",style={'fontSize':17,"margin-top": "20px","margin-left": "33px","margin-right": "50px","color": "white",'textAlign':'justify',} ))                                
    ]),



    dbc.Row([
        dbc.Col(html.Div("2. RandomForestClassifier",style={'fontSize':22,"margin-top": "30px","margin-left": "30px","margin-right": "50px","color": "white",'textAlign':'justify',} ))                                
    ]),
    dbc.Row([
        dbc.Col(html.Div("The random forest classifier is a supervised learning algorithm which you can use for regression and classification problems. It is among the most popular machine learning algorithms due to its high flexibility and ease of implementation. Why is the random forest classifier called the random forest? That’s because it consists of multiple decision trees just as a forest has many trees. On top of that, it uses randomness to enhance its accuracy and combat overfitting, which can be a huge issue for such a sophisticated algorithm. These algorithms make decision trees based on a random selection of data samples and get predictions from every tree. After that, they select the best viable solution through votes. It has numerous applications in our daily lives such as feature selectors, recommender systems, and image classifiers. Some of its real-life applications include fraud detection, classification of loan applications, and disease prediction. It forms the basis for the Boruta algorithm, which picks vital features in a dataset. ",style={'fontSize':17,"margin-top": "20px","margin-left": "33px","margin-right": "50px","color": "white",'textAlign':'justify',} ))                                
    ]),  


    dbc.Row([
        dbc.Col(html.Div("3. KNeighbors Classifier",style={'fontSize':22,"margin-top": "30px","margin-left": "30px","margin-right": "50px","color": "white",'textAlign':'justify',} ))                                
    ]),
    dbc.Row([
        dbc.Col(html.Div("K-Nearest Neighbours is one of the most basic yet essential classification algorithms in Machine Learning. It belongs to the supervised learning domain and finds intense application in pattern recognition, data mining and intrusion detection. It is widely disposable in real-life scenarios since it is non-parametric, meaning, it does not make any underlying assumptions about the distribution of data (as opposed to other algorithms such as GMM, which assume a Gaussian distribution of the given data). We are given some prior data (also called training data), which classifies coordinates into groups identified by an attribute.",style={'fontSize':17,"margin-top": "30px","margin-left": "33px","margin-right": "50px","color": "white",'textAlign':'justify',} ))                                
    ]), 
])