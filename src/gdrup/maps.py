# -*- coding: utf-8 -*-
"""
Created the 13/12/2022

@author: Sebastien Weber
"""
import random
from typing import Tuple, List

import dash
from dash import html, dcc

import dash_leaflet as dl
import dash_leaflet.express as dlx
from dash_extensions.javascript import assign
from yattag import Doc



def get_popup_from_card(data_card):
    doc, tag, text = Doc().tagtext()
    with tag('a', href=data_card['lab_url']):
        text(data_card['lab_acronym'])
    with tag('p'):
        text(data_card['city'])
        with tag('ul'):
            for theme in data_card['themes']:
                with tag('li'):
                    text(theme)
    return doc.getvalue()


def get_geo_from_data_card(data_cards: List[dict]) -> dl.GeoJSON:
    # Create some markers.
    data = dlx.dicts_to_geojson([dict(**data['coordinates'],
                                      popup=get_popup_from_card(data),
                                      tooltip=data['lab_acronym']) for data in data_cards])
    # Create geojson.
    return dl.GeoJSON(data=data, cluster=True, zoomToBoundsOnClick=True)


ignApiKey = 'pratique'
ignLayer = 'GEOGRAPHICALGRIDSYSTEMS.PLANIGNV2'
satelite_layer = 'ORTHOIMAGERY.ORTHOPHOTOS'
style = 'normal'
format_ign = 'image/png'
format_photo = 'image/jpeg'
service = 'WMTS'

plan_layer = dl.TileLayer(url=f'https://wxs.ign.fr/{ignApiKey}/geoportail/wmts?' +
                             f'&REQUEST=GetTile&SERVICE=WMTS&VERSION=1.0.0&TILEMATRIXSET=PM' +
                             f'&LAYER={ignLayer}&STYLE={style}&FORMAT={format_ign}' +
                             '&TILECOL={x}&TILEROW={y}&TILEMATRIX={z}')

photo_layer = dl.TileLayer(url=f'https://wxs.ign.fr/{ignApiKey}/geoportail/wmts?' +
                             f'&REQUEST=GetTile&SERVICE=WMTS&VERSION=1.0.0&TILEMATRIXSET=PM' +
                             f'&LAYER={satelite_layer}&STYLE={style}&FORMAT={format_photo}' +
                             '&TILECOL={x}&TILEROW={y}&TILEMATRIX={z}')

layers = [dl.BaseLayer(plan_layer, name='plan', checked=True),
          dl.BaseLayer(photo_layer, name='photo', checked=False),
          dl.BaseLayer(dl.TileLayer(), name='OSM', checked=False),
          ]


