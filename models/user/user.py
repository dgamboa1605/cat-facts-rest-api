# pylint: disable=R0903
"""
Module for defining the 'User' data model using Pydantic.
"""

from pydantic import BaseModel, Field
from models.user.name import Name

class User(BaseModel):
    """
    Represents a user entity.
    """
    id: str = Field(..., alias="_id")
    name: Name
    photo: str

    class Config:
        """
        Pydantic configuration for the Fact model.

        Attributes:
            allow_population_by_field_name (bool): Allows population of fields by their field names
            rather than their aliases. Default is True.
        """
        allow_population_by_field_name = True
