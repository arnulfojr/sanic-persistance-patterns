# flake8: noqa
from sanic import Blueprint


blueprint = Blueprint('todo', url_prefix='/todo')

# import controllers
from todo import controller
