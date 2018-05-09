import peewee
from datetime import datetime

from uuid import uuid4

from lib.mysql.db import database


class ToDo(peewee.Model):
    """To Do."""
    id = peewee.UUIDField(primary_key=True, default=uuid4)

    text = peewee.CharField()

    created_on = peewee.DateTimeField(default=datetime.now)

    class Meta:
        database = database
