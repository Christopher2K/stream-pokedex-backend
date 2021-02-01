from app.models import User
from app.schemas import authentication, common
from fastapi import APIRouter, HTTPException
from firebase_admin import auth

router = APIRouter(prefix="/auth")


@router.post("/signup", response_model=common.SuccessWithoutData)
async def signup(data: authentication.SignupIn):
    try:
        user = auth.create_user(
            email=data.email,
            password=data.password,
            display_name=data.username,
            email_verified=True,
        )

        await User.create(
            username=data.username,
            firebase_id=user.uid,
        )

        return common.SuccessWithoutData()
    except Exception as e:
        print(e)
        raise HTTPException(500, "signup_error")


async def get_profile():
    pass
