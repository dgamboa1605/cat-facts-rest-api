from pydantic import BaseModel
from models.fact.status import Status


class Fact(BaseModel):
    _id: str
    user: str
    text: str
    type: str
    deleted: bool
    createdAt: str
    updatedAt: str
    __v: int
    status: Status
