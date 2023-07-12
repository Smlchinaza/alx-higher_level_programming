class Student:
    """Class that defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a student with first_name, last_name, and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieve a dictionary representation of a Student instance"""
        attributes = {}
        attributes['first_name'] = self.first_name
        attributes['last_name'] = self.last_name
        attributes['age'] = self.age
        return attributes
