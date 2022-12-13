import random
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import dash_leaflet as dl

from gdrup.maps import layers, get_geo_from_data_card
from gdrup.cards import CardContainer, data_gdr

if __name__ != '__main__':
    from django_plotly_dash import DjangoDash

    app = DjangoDash('Map')   # replaces dash.Dash

else:
    app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

map_with_tiles = dl.Map([dl.LayersControl(layers),
                         get_geo_from_data_card(data_gdr)
                         ], center=(45, 1.4), zoom=6)  # , style={'height': '100vh'})
card_container = CardContainer()

row = html.Div([
    dbc.Row(dbc.Col(html.Div([html.H1(children='GDR UP Cartography')]), lg={"size": 6, "offset": 3})),
    dbc.Row(dbc.Col(dcc.Dropdown(['New York City', 'Montréal', 'San Francisco'], 'Montréal', multi=True))),
    dbc.Row([
        dbc.Col(map_with_tiles, width=8),
        dbc.Col(html.Div(children=card_container.create_cards()), width=4)],
    )],)

app.layout = row

if __name__ == '__main__':
    app.run_server()