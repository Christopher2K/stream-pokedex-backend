from typing import List
from uuid import UUID

from app.dependencies import get_authenticated_user
from app.models import Favorite, Pokemon, User
from app.schemas import FavoriteOut, NewFavoriteIn, SuccessWithoutData
from fastapi import APIRouter, Depends, HTTPException
from tortoise.exceptions import DoesNotExist

router = APIRouter(prefix="/favorite")


@router.get("", response_model=List[FavoriteOut])
async def get_user_favorites(
    current_user: User = Depends(get_authenticated_user),
):
    user_fav = await Favorite.filter(user=current_user).prefetch_related(
        "pokemon",
    )
    return user_fav


@router.post("", response_model=SuccessWithoutData)
async def add_new_favorite(
    data: NewFavoriteIn,
    current_user: User = Depends(get_authenticated_user),
):
    try:
        pokemon = await Pokemon.get(id=data.pokemon_id)
    except DoesNotExist:
        raise HTTPException(404, "Pokemon does not exist")

    existing_favorite = await Favorite.get_or_none(
        pokemon__id=data.pokemon_id, user=current_user
    )

    if existing_favorite is None:
        await Favorite.create(user=current_user, pokemon=pokemon)

    return SuccessWithoutData()


@router.delete("/{favorite_id}", response_model=SuccessWithoutData)
async def remove_from_favorites(
    favorite_id: UUID, current_user: User = Depends(get_authenticated_user)
):
    await Favorite.filter(id=favorite_id, user=current_user).delete()
    return SuccessWithoutData()
