from flask import Blueprint

API = Blueprint('api', __name__)
from . import graphql_routes
