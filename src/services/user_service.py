from typing import List

from passlib.context import CryptContext
from sqlmodel import Session, select

from src.models.user import User
from src.shemats.user_chemat import UserInput, UserOutput


class UserService:
    def __init__(self, db: Session):
        self.db = db
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def create_user(self, user: UserInput) -> UserOutput:
        user = User(**user.model_dump(exclude_none=True))  # Créer l'objet User
        self.db.add(user)  # Ajouter l'utilisateur à la session
        self.db.commit()  # Commiter la transaction
        self.db.refresh(user)  # Rafraîchir les données de l'utilisateur
        return UserOutput(id=user.id, email=user.email)

    def all_users(self):
        statement = select(User)
        users = self.db.exec(statement)
        return users


