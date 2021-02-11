from uuid import UUID

from pydantic import BaseModel

from .pokemon import PokemonOut


class FavoriteOut(BaseModel):
    id: UUID
    pokemon: PokemonOut

    class Config:
        orm_mode = True


class NewFavoriteIn(BaseModel):
    pokemon_id: UUID
