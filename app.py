from dash import Dash, html, dcc, callback, Output, Input, dash_table
import plotly.express as px
import pandas as pd
import numpy as np

from src.movietable import movie_table

df = pd.read_csv('/workspaces/MoviesAreFun/data/movies_metadata.csv')

dash_app = Dash(__name__)

app = dash_app.server

dash_app.layout = html.Div([
    html.H1(children='Movies are fun', style={'textAlign':'center'}),
    html.Div(
        dcc.Dropdown(np.sort(df.original_title.unique()), 'Gladiator', id='title-selection'),
        style = {"width": "300px"}
    ),
    html.Br(),
    html.Div(id='title-overview'),
    html.Br(),
    movie_table(df)
])

@callback(
    Output('title-overview', 'children'),
    Input('title-selection', 'value')
)
def update_overview(value):
    """input is original_title, returns title overview
    
    """

    dff = df[df.original_title == value]

    overview = dff.overview

    return overview

if __name__ == '__main__':
    dash_app.run_server(debug=True)
