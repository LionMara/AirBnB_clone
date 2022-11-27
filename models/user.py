#!/usr/bin/python3
"""
user class
"""
from models.base_model import BaseModel

class User(BaseModel):
    """user class inherits from BaseModel
    attributes:
    email: a public class attribute for users email
    password: public class attribute for user password
    first_name: public class attribute for user first name
    last_name: public class attribute for user last name
    oh and all the attributes are strings
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        init method for the user class

        attributes:
        args: a list with arguments
        kwargs: a dictionary with arguments
        """
        super().__init__(*args, **kwargs)