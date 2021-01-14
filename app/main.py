from typing import List

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app import settings
from app.models import Pokemon
from app.schemas import PokemonOut

root = FastAPI()


@root.get("/")
def read_root():
    return {"Hello": "World"}


@root.get("/pokemons", response_model=List[PokemonOut])
async def get_pokemons():
    pokemons_list = await Pokemon.all()
    return pokemons_list


register_tortoise(
    root,
    db_url=settings.DATABASE_URL,
    modules={"models": ["app.models"]},
    generate_schemas=False,
    add_exception_handlers=True,
)
