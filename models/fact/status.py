from pydantic import BaseModel
from typing import Optional


class Status(BaseModel):
    verified: Optional[bool]
    sentCount: int
