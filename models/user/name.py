"""
Module for defining the 'Name' data model using Pydantic.
"""

from pydantic import BaseModel

class Name(BaseModel):
    """
    Represents a name entity.
    """
    first: str
    last: str
