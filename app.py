from flask import Flask
from dash import Dash, html, dcc 
import plotly.graph objs as go
import pandas as pd

app = Dash(_name_)

def serve_layout():
df = pd.read_excel('portalwiki.xlsx')
return html.Div([html.H1(df['Titulo']),
                 html.Div(df['Tema1']),
                 html.Div(df['Tema2'])])
                 

app.layout =serve_layout

if_name== 'main_':

app.run_server(host='0,0,0,0',port=80)
