from sanic import Blueprint

from .users import users

api = Blueprint.group(users, url_prefix="/api")
