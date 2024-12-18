from typing import Optional
from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    id: Optional[int] = Field(None, primary_key=True)
    email: str
    hashed_password: str
    # validation_code: Optional[str] = Field(None)
    # validation_code_expires_at: Optional[datetime] = Field(None)
