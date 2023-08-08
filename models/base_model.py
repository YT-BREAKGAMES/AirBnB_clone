#!/usr/bin/python3

"""Define a class BaseModel that defines all common attributes/methods for other classes"""

import uuid
from datetime import date, datetime


class BaseModel:
    """defines all common attributes/methods for other classes"""

    def __init__(self):
        """initializes a new instance of base model"""
        self.id = str(uuid.uuid4())
        tnow = datetime.now()
        self.created_at = tnow
        self.updated_at = tnow

    def __str__(self):
        """returns a string representation of an instance"""
        name = self.__class__.__name__
        return f"[{name}] ({self.id}) {self.__dict__}"
