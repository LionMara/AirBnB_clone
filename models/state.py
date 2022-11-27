#!/usr/bin/python3
"""module containing the state class"""

from models.base_model import BaseModel

class State(BaseModel):
    """
    inherits from BaseModel
    public class attribute:
        name(str)
    """
    name = ""