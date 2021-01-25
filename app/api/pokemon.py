from typing import List

from app.models import Pokemon
from app.schemas import PokemonOut
from fastapi import APIRouter

router = APIRouter(prefix="/pokemon")


@router.get("", response_model=List[PokemonOut])
async def get_pokemons(query: str = None):
    if query is None:
        pokemons_list = await Pokemon.all()
        return pokemons_list
    else:
        search_result = await Pokemon.filter(name__istartswith=query)
        return search_result
