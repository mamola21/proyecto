from dash import Dash, html, dcc
import pandas as pd
import plotly.graph_objs as go

# Declarar objetos principales
app = Dash(_name_)

# Cargar la base de datos
def serve_layout():
  df = pd.read_excel('portalwiki.xlsx')
  return html.Div([html.H1(df['Titulo']),
                       html.Div(df['Tema1']),
                       html.Div(df['Tema2'])])                
#funcion principal
app.layout = serve_layout

if _name_ == '_main_':
  #Cargar el objeto principal a todas las interfaces de red en el puerto 80
  app.run_server(host='0.0.0.0',port=80)
