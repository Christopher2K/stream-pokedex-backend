from pydantic import BaseModel


class SignupIn(BaseModel):
    email: str
    password: str
    username: str
