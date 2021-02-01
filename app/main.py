from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise

from app import settings
from app.api import pokemon_router

root = FastAPI()

origins = [
    "http://127.0.0.1:3000",
    "http://localhost:3000",
]

root.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
