from typing import Union
from uuid import UUID

from app.models import PokemonType
from pydantic import BaseModel


class PokemonOut(BaseModel):
    id: UUID
    name: str
    number: int
    main_type: PokemonType
    secondary_type: Union[PokemonType, None]
    hp: int
    atk: int
    defense: int
    spe_atk: int
    spe_def: int
    speed: int
    generation: int
    legendary: bool

    class Config:
        orm_mode = True
