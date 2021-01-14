from typing import TYPE_CHECKING

from tortoise import fields
from tortoise.models import Model

if TYPE_CHECKING:
    from app.models.pokemon import Pokemon


class Team(Model):
    id = fields.UUIDField(pk=True)
    name = fields.CharField(max_length=255)
    user = fields.ForeignKeyField("models.User", related_name="teams")
    pokemons: fields.ManyToManyRelation["Pokemon"] = fields.ManyToManyField(
        "models.Pokemon",
        through="PokemonTeam",
        backward_key="team_id",
        forward_key="pokemon_id",
    )

    class Meta:
        table = "Team"
