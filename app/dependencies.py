from typing import Optional

from fastapi import Header, HTTPException, status
from firebase_admin import auth

from app.models import User


async def get_authenticated_user(authorization: Optional[str] = Header(None)):
    unauthorized_exp = HTTPException(
        status.HTTP_401_UNAUTHORIZED,
        "Unauthorized",
    )

    if authorization is not None:
        _, token = authorization.split(" ")
        uid = None

        try:
            decoded = auth.verify_id_token(token)
            uid = decoded["uid"]
        except Exception as e:
            print(e)
            raise unauthorized_exp

        user = await User.get(firebase_id=uid)
        return user
    else:
        raise unauthorized_exp
