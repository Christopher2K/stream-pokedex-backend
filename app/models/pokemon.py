from enum import Enum

from tortoise import fields
from tortoise.models import Model


class PokemonType(Enum):
    Bug = "Bug"
    Fire = "Fire"
    Normal = "Normal"
    Dark = "Dark"
    Flying = "Flying"
    Poison = "Poison"
    Dragon = "Dragon"
    Ghost = "Ghost"
    Psychic = "Psychic"
    Electric = "Electric"
    Grass = "Grass"
    Rock = "Rock"
    Fairy = "Fairy"
    Ground = "Ground"
    Steel = "Steel"
    Fighting = "Fighting"
    Ice = "Ice"
    Wate = "Water"


class Pokemon(Model):
    id = fields.UUIDField(pk=True)
    name = fields.CharField(max_length=255, null=False)
    number = fields.IntField(null=False, unique=True)
    main_type = fields.CharEnumField(PokemonType, max_length=50, null=False)
    secondary_type = fields.CharEnumField(
        PokemonType,
        max_length=50,
        null=True,
    )
    hp = fields.IntField(null=False)
    atk = fields.IntField(null=False)
    defense = fields.IntField(null=False, source_field="def")
    spe_atk = fields.IntField(null=False)
    spe_def = fields.IntField(null=False)
    speed = fields.IntField(null=False)
    generation = fields.IntField(null=False)
    legendary = fields.BooleanField(null=False)

    def __str__(self) -> str:
        return self.name

    class Meta:
        table = "Pokemon"
