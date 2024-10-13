#!/bin/python3

# library_system.py

class Book:
    def __init__(self, title: str, author: str):
        """Initialize the Book attributes."""
        self.title = title
        self.author = author

    def __str__(self):
        """String representation of the Book instance."""
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        """Initialize the EBook attributes, including those from the base class."""
        super().__init__(title, author)
        self.file_size = file_size  # in KB

    def __str__(self):
        """String representation of the EBook instance."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        """Initialize the PrintBook attributes, including those from the base class."""
        super().__init__(title, author)
        self.page_count = page_count  # number of pages

    def __str__(self):
        """String representation of the PrintBook instance."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    def __init__(self):
        """Initialize an empty library."""
        self.books = []  # List to store books

    def add_book(self, book: Book):
        """Add a Book, EBook, or PrintBook instance to the library."""
        self.books.append(book)

    def list_books(self):
        """Print details of each book in the library."""
        for book in self.books:
            print(book)
