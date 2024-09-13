from pydantic import BaseModel
from models.user.name_model import NameModel

class UserModel(BaseModel):
    _id: str
    name: NameModel
    photo: str
