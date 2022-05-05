from dash import Dash, html, dcc
import pandas as pd

app = Dash(__name__)
app.layout = html.Div([html.H1('Ingenieria de sistemas'),
                       html.Div('¿Qué es?')
                       html.Div('Es la rama de la ingeniería relacionada con el manejo de las tecnologías y los sistemas de información.')
                       html.Div('Esta contempla las bases teóricas y metodológicas necesarias para el diseño, la implantación, el análisis,')
                       html.Div('el control, el procesamiento,el transporte, la operatividad, la toma de decisiones y la búsqueda de seguridad de los')
                       html.Div('sistemas informáticos')
                       
app.layout = serve_layout
if __name__ == '__main__':
app.run_server(host='0.0.0.0',port=80)
