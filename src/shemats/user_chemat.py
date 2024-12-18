from pydantic import BaseModel


class UserInput(BaseModel):
    email: str
    hashed_password: str


class UserOutput(BaseModel):
    id: int
    email: str

    class Config:
        from_attributes = True
