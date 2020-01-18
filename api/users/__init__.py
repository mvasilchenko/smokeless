from sanic import Blueprint

from .signup import signup

users = Blueprint.group(signup, url_prefix="/users")