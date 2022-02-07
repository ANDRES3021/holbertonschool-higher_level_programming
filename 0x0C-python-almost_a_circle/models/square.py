#!/usr/bin/python3
"""This is the Square module.
Contains the Square class that inherits from Rectangle.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This class inherits from Rectangle and defines a Square object."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the default attributes of the Base object."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overrides the default behaviour of the __str__ method."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Get and Set the size attribute of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the Square attributes."""
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]

        else:
            for key, value in kwargs.items():
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
                if key == "id":
                    self.id = value

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        return{"id": self.id, "x": self.x, "size": self.width, "y": self.y}
