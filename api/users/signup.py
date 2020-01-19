from sanic import Blueprint, response

from sanic_transmute import describe, add_route

from .models import UserModel
from .serializers import UserSchema

signup = Blueprint("api_signup", url_prefix="/signup")


# @describe(paths="/", methods=["GET", "POST"])
@signup.route("/", methods=["POST"])
async def signup_root(request) -> dict:
    if request.method == "POST":
        user = UserSchema(request.json)

        user.validate()
        is_uniq = await UserModel.is_unique(doc=dict(name=user.name))
        if is_uniq in (True, None):
            await UserModel.insert_one(user.to_native())
            result = response.json({"success": True})
            return result
        else:
            return response.json({"success": False}, status=200)
