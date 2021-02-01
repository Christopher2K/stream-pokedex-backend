from pydantic import BaseModel


class SuccessWithoutData(BaseModel):
    status: str = "success"
