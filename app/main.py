from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app import settings
from app.api import pokemon_router

root = FastAPI()


@root.get("/")
def read_root():
    return {"Hello": "World"}


root.include_router(pokemon_router)


register_tortoise(
    root,
    db_url=settings.DATABASE_URL,
    modules={"models": ["app.models"]},
    generate_schemas=False,
    add_exception_handlers=True,
)
