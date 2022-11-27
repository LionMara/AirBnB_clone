#!/usr/bin/python3
"""
module containing the amenity class
"""
from models.base_model import BaseModel

class Amenity(BaseModel):
    """
    inherits from the BaseModel
    public class attribute:
    name(str)
    """

    name = ""