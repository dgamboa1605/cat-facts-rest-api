# pylint: disable=R0903
"""
This module defines the `Fact` class, which is a Pydantic model representing a fact entity.
"""

from pydantic import BaseModel, Field
from models.fact.status import Status


class Fact(BaseModel):
    """
    Represents a fact entity.
    """
    id: str = Field(..., alias="_id")
    user: str
    text: str
    type: str
    deleted: bool
    createdAt: str
    updatedAt: str
    v: int = Field(..., alias="__v")
    status: Status

    class Config:
        """
        Pydantic configuration for the Fact model.

        Attributes:
            allow_population_by_field_name (bool): Allows population of fields by their field names
            rather than their aliases. Default is True.
        """
        allow_population_by_field_name = True
