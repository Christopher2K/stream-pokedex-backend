from tortoise import fields
from tortoise.models import Model


class Favorite(Model):
    id = fields.UUIDField(pk=True)
    user = fields.ForeignKeyField(
        "models.User",
        related_name="favorites",
    )
    pokemon = fields.ForeignKeyField("models.Pokemon")

    class Meta:
        table = "Favorite"
