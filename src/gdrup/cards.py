# -*- coding: utf-8 -*-
"""
Created the 13/12/2022

@author: Sebastien Weber
"""
from typing import List
from dash import html
import dash_bootstrap_components as dbc


data_gdr = [dict(lab_acronym='CEMES',
                 lab='Centre d\'Ellaboration de Matériaux et d\'Etudes Structurales',
                 lab_url='https://www.cemes.fr/',
                 city='Toulouse',
                 group='Ultrafast Electron Microscopy',
                 people=['A. Arbouet', 'S. Weber'],
                 themes=['optics', 'biers', 'surf'],
                 tutelles=['CNRS', 'Université de Toulouse'],
                 description='A cool group doing awesome stuff',
                 coordinates=dict(lat=43.5790697, lon=1.4603482)),

            dict(lab_acronym='Lidyl',
                 lab='Laboratoire Interactions, Dynamiques et Lasers',
                 lab_url='https://iramis.cea.fr/LIDYL/',
                 city='Gif-Sur-Yvette',
                 group='Group 1',
                 people=['P. Salières', 'T. Ruchon'],
                 themes=['optics', 'biers', 'surf'],
                 tutelles=['CEA'],
                 description='A cool group doing awesome stuff',
                 coordinates=dict(lat=48.7079648, lon=2.1453727)),

            dict(lab_acronym='CELIA',
                 lab_url='https://www.celia.u-bordeaux.fr',
                 lab='Centre',
                 city='Pessac',
                 group='Dyna',
                 people=['V. Blanchet', 'Y. Mairesse'],
                 themes=['optics', 'biers', 'surf'],
                 tutelles=['CNRS', 'Université de Bordeaux'],
                 description='A cool group doing awesome stuff',
                 coordinates=dict(lat=44.80959, lon=-0.5953324))
            ]


class DataCard:
    def __init__(self, lab_acronym: str, lab: str, lab_url: str, city: str, group: str,
                 people: List[str], themes: List[str], tutelles: List['str'], description: str = '',
                 coordinates: dict = dict(lat=43.5790697, long=1.4603482)):
        self.lab = lab
        self.lab_acronym = lab_acronym
        self.lab_url = lab_url
        self.city = city
        self.group = group
        self.people = people[:]
        self.themes = themes[:]
        self.tutelles = tutelles[:]
        self.description = description
        self.coordinates = coordinates

    def create_card(self):
        return dbc.Card(
            dbc.CardBody(
                [html.H3(self.lab_acronym, className="card-title"),
                 html.H6(html.A(children=self.lab, href=self.lab_url, target='_blank')),
                 html.H6(self.city),
                 html.P(str(self.people)),
                 html.P(self.description, className="card-text",),]
            ),
        )

    def __call__(self, *args, **kwargs):
        return self.create_card()


class CardContainer:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def create_cards(self, children: List[dict] = None):
        if children is None:
            children = data_gdr
        div_content = []
        for child in children:
            card = DataCard(**child)
            div_content.append(dbc.Row(card.create_card()))
        return div_content