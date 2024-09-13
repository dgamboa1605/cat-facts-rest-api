from pydantic import BaseModel

class NameModel(BaseModel):
    first: str
    last: str
