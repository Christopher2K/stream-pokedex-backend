from app.models import User
from app.schemas import authentication, common
from fastapi import APIRouter, HTTPException
from firebase_admin import auth, exceptions

router = APIRouter(prefix="/auth")

error_dict = {
    "ALREADY_EXISTS": {
        "status": 400,
        "message": "already_exists",
    }
}


@router.post("/signup", response_model=common.SuccessWithoutData)
async def signup(data: authentication.SignupIn):
    maybe_existing_user = await User.filter(username=data.username)
    if len(maybe_existing_user) > 0:
        raise HTTPException(
            error_dict["ALREADY_EXISTS"]["status"],
            error_dict["ALREADY_EXISTS"]["message"],
        )

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
    except exceptions.FirebaseError as e:
        if e.code in error_dict.keys():
            raise HTTPException(
                error_dict[e.code]["status"], error_dict[e.code]["message"]
            )
        else:
            raise HTTPException(500, "signup_error")
    except Exception as e:
        print(e)
        raise HTTPException(500, "signup_error")


async def get_profile():
    pass
