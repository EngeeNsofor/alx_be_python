#!/bin/python3

class Book:
    def __init__(self, title: str, author: str, year: int):
        """Constructor to initialize the Book instance."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor that is called when the object is about to be destroyed."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """String representation of the Book instance."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official representation of the Book instance for debugging."""
        return f"Book('{self.title}', '{self.author}', {self.year})"

