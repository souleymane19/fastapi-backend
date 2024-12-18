from typing import List

from fastapi import APIRouter, Depends
from sqlmodel import Session

from src.shemats.user_chemat import UserInput, UserOutput
from src.services.user_service import UserService
from src.config.db import get_db

router = APIRouter()

# user_service = UserService(get_db())


@router.post("/")
def create_user(user: UserInput, db: Session = Depends(get_db)) -> UserOutput:
    user_service = UserService(db)
    return user_service.create_user(user)


@router.get("/",  response_model=List[UserOutput])
def all_users(db: Session = Depends(get_db)):
    user_service = UserService(db)
    return user_service.all_users()

#
# @router.post("/{user_id}")
# def update_user(user_id: int, user: UserInput) -> UserOutput:
#     user = user_service.update_user(user_id, user)
#     return user
#
#
# @router.get("/{user_id}")
# def delete_user(user_id: int) -> UserOutput:
#     user = user_service.delete_user(user_id)
#     return user
