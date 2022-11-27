#!/usr/bin/python3
"""
this module contains a class BaseModel that defines all
common attributes/methods for other classes:
"""
from datetime import datetime
from uuid import uuid4
import models
class BaseModel():
    """
    this is the BaseModel class and it defines  all the common
    attributes/methods for other classes

    methods:
        __init__(self, *args, **kwargs)
        __str__(self)
        __save(self)
        __repr__(self)
        to_dict(self)

    """
    def __init__(self, *args, **kwargs):
        """
        initialize attributes: randon uuid, dates created/updated
        """
        if kwargs:
            for key, value in kwargs.items():
                if "created_at" == key:
                    self.created_at = datetime.strptime(kwargs["created_at"],\
                         "%Y-%m-%dT%H:%M:%S.%f")
                elif "updated_at" == key:
                    self.updated_at = datetime.strptime(kwargs["updated_at"],\
                        "%Y-%m-%dT%H:%M:%S.%f")
                elif "__class__" == key:
                    pass
                else:
                    setattr(self, key, value)
        
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        return string of info about model
        """
        return ("[{}] ({}) {}"\
            .format(self.__class__.__name__, self.id, self.__dict__))
    def __repr__(self):
        """
        returns string representation
        """
        return (self.__str__())

    def save(self):
        """
        update instance with updated time and save
        to serialized file
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        return dic with string formats of times;
        and class info to dic
        """
        dic = {}
        dic["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if isinstance(value, datetime()):
                dic[key] = value.isoformat()
            else:
                dic[key] = value

        return dic