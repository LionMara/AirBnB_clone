#!/usr/bin/python3
"""file storage"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
	"""serializes and deserializes json files"""

	__file_path = 'file.json'
	__objects = {}

	class_dict = {"BaseModel": BaseModel, "User": User, "Place": Place,
                  "Amenity": Amenity, "City": City, "Review": Review,
                  "State": State}

	def all(self):
		"""return dictionary of <class>.<id> : object instance"""
		return self.__objects
	
	def new(self, obj):
		"""add new obj to existing dictionary of instances"""
		if obj:
			key = "{}.{}".format(obj.__class__.__name__, obj.id)
			self.__objects[key] = obj

	def save(self):
		"""save dictionaries to JSON file"""
		my_dict = {}

		for key, obj in self.__objects.items():
			my_dict[key] = obj.to_dict()
		with open(self.__file_path, 'w') as f:
			json.dump(my_dict, f)

	def reload(self):
		"""if json file exists, convert obj dicts back to instances"""
		try:
			with open(self.__file_path, 'r') as f:
				new_obj = json.load(f)
			for key, value in new_obj.items():
				obj = self.class_dict[value["__class__"]](**value)
				self.__objects[key] = obj
		except FileNotFoundError:
			pass