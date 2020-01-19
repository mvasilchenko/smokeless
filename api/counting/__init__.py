from sanic import Blueprint

from .smoke import smoke

counting = Blueprint.group(smoke, url_prefix="/counting")
