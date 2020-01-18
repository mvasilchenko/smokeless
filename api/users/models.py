from sanic_motor import BaseModel


class UserModel(BaseModel):
    __coll__ = 'users'
    __unique_fields__ = ['name']

    async def validate_name(self, name: str) -> bool:
        if name:
            is_uniq = await self.is_unique(doc=dict(name=name))
            if is_uniq:
                return True
