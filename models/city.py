#!/usr/bin/python3
"""
module containing the city class
"""

from models.base_model import BaseModel

class City(BaseModel):
    """
    inherits from BaseModel
    Public class attributes:
    state_id: (str) will be the state.id
    name:(str)
    """
    state_id = ""
    name = ""