# pylint: disable=R0903
"""
This module contains the definition of the FactResponse class, which is used to
represent the response structure for facts in the application. It utilizes Pydantic
for data validation and parsing.
"""

from typing import Optional
from pydantic import BaseModel, Field
from models.fact.status import Status
from models.user.user import User


class FactResponse(BaseModel):
    """
    Represents a fact response entity.
    """
    id: str = Field(..., alias="_id")
    user: User
    text: str
    type: str
    source: str
    deleted: Optional[bool]
    createdAt: str
    updatedAt: str
    v: int = Field(..., alias="__v")
    status: Status
    used: bool

    class Config:
        """
        Pydantic configuration for the Fact model.

        Attributes:
            allow_population_by_field_name (bool): Allows population of fields by their field names
            rather than their aliases. Default is True.
        """
        allow_population_by_field_name = True
