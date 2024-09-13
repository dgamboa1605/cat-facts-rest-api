"""
Module for defining the 'Status' data model using Pydantic.
"""

from typing import Optional
from pydantic import BaseModel


class Status(BaseModel):
    """
    Represents a status entity.
    """
    verified: Optional[bool]
    sentCount: int
