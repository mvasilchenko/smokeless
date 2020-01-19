from datetime import datetime

from schematics.models import Model
from schematics.types import StringType, DateTimeType, IntType


class SmokeSchema(Model):
    user_id = StringType(required=True)
    created_at = DateTimeType(default=datetime.now())
