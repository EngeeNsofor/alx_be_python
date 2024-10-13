#!/bin/python3

import math

class Shape:
    def area(self):
        """Method to calculate the area, should be overridden in derived classes."""
        raise NotImplementedError("This method should be overridden by subclasses.")

class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        """Initialize the Rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Override the area method to calculate the area of the rectangle."""
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius: float):
        """Initialize the Circle with radius."""
        self.radius = radius

    def area(self):
        """Override the area method to calculate the area of the circle."""
        return math.pi * (self.radius ** 2)
