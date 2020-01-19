from datetime import datetime

from sanic_motor import BaseModel


class UserModel(BaseModel):
    __coll__ = 'users'
    __unique_fields__ = ['name']

    async def validate_name(self, name: str) -> bool:
        if name:
            is_uniq = await self.is_unique(doc=dict(name=name))
            if is_uniq:
                return True

    @classmethod
    async def created_at_week(cls, _id: int) -> int:
        cursor = await cls.find_one(_id)
        created_at_isodate = cursor.created_at
        num_of_week = created_at_isodate.isocalendar()[1]
        return num_of_week

    @staticmethod
    async def current_week() -> int:
        return datetime.now().isocalendar()[1]

    @classmethod
    async def current_cigarette_day_limit(cls, _id: int) -> int:
        default_limit = 20
        current_week = await cls.current_week()
        created_at_week = await cls.current_week()
        return default_limit - (current_week - created_at_week)
