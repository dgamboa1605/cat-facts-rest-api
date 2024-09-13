from pydantic import BaseModel, Field
from models.fact.status import Status
from models.user.user_model import UserModel


class FactResponse(BaseModel):
    id: str = Field(..., alias="_id")
    user: UserModel
    text: str
    type: str
    source: str
    deleted: bool
    createdAt: str
    updatedAt: str
    __v: int
    status: Status
    used: bool

    class Config:
        allow_population_by_field_name = True
