from datetime import datetime

from sanic import Blueprint
from sanic.response import json


from api.counting.models import SmokeModel
from api.counting.serializers import SmokeSchema

smoke = Blueprint("api_smoke", url_prefix="/smoke")


@smoke.route(uri="/<user_id>", methods=["POST", "GET"])
async def smoke_root(request, user_id: int) -> SmokeSchema or dict:
    if request.method == "POST":
        smoke_instance = SmokeSchema(request.json)
        smoke_instance.user_id = user_id
        smoke_instance.validate()
        cigarette_balance = await SmokeModel.cigarettes_balance_for_today(user_id)
        await SmokeModel.insert_one(smoke_instance.to_native())
        return json({"cigarette_balance": cigarette_balance})
    elif request.method == "GET":
        date = datetime(2020, 1, 18, 1, 1, 1)
        cursor = await SmokeModel.find_one({'created_at': {'$gte': date}})

        return cursor