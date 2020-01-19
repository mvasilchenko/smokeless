from sanic import Blueprint

from .users import users
from .counting import counting

api = Blueprint.group(users,counting, url_prefix="/api")
