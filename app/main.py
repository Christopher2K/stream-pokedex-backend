from fastapi import FastAPI

root = FastAPI()


@root.get("/")
def read_root():
    return {"Hello": "World"}
