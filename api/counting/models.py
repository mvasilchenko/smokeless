from datetime import datetime, date

from sanic_motor import BaseModel

from api.users.models import UserModel


class SmokeModel(BaseModel):
    __coll__ = "smoke"

    @classmethod
    async def already_smoked_today(cls, user_id: int):
        today = date.today()
        today = datetime(today.year, today.month, today.day, 0, 0, 0)

        count = await cls.count({"user_id": user_id, "created_at": {"$gte": today}})
        return count

    @classmethod
    async def cigarettes_balance_for_today(cls, user_id: int):
        current_limit = await UserModel.current_cigarette_day_limit(user_id)
        already_smoked = await cls.already_smoked_today(user_id)
        return current_limit - already_smoked
