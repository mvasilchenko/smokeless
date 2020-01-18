from sanic import Blueprint

from sanic_transmute import describe, add_route

from .models import UserModel
from .serializers import UserSchema

signup = Blueprint("api_signup", url_prefix="/signup")


@describe(paths="/", methods=["GET", "POST"])
async def signup_root(request) -> UserSchema or dict:
    if request.method == "POST":
        user = UserSchema(request.json)

        user.validate()
        is_uniq = await UserModel.is_unique(doc=dict(name=user.name))
        if is_uniq in (True, None):
            await UserModel.insert_one(user.to_native())
        else:
            return {"success": False}

        return user

add_route(signup, signup_root)
