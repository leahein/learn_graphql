from flask import Flask
from flask import Blueprint
from flask_graphql import GraphQLView

from ..schema import SCHEMA
from . import API

API.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=SCHEMA,
        graphiql=True,
    )
)

