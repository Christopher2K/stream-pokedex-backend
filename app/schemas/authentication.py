from uuid import UUID

from pydantic import BaseModel


class SignupIn(BaseModel):
    email: str
    password: str
    username: str


class UserOut(BaseModel):
    id: UUID
    username: str

    class Config:
        orm_mode = True
