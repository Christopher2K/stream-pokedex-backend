from typing import TYPE_CHECKING

from tortoise import fields
from tortoise.models import Model

if TYPE_CHECKING:
    from app.models.favorite import Favorite
    from app.models.team import Team


class User(Model):
    id = fields.UUIDField(pk=True)
    username = fields.CharField(max_length=20, null=False, unique=True)
    firebase_id = fields.CharField(max_length=255, null=False, unique=True)

    favorites: fields.ReverseRelation["Favorite"]
    teams: fields.ReverseRelation["Team"]

    class Meta:
        table = "User"
