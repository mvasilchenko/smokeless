from datetime import datetime

from schematics.models import Model
from schematics.types import StringType, IntType, DateTimeType


class UserSchema(Model):
    name = StringType(required=True)
    _id = IntType(required=True)
    created_at = DateTimeType(default=datetime.now())
