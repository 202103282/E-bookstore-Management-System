# Ebook.py

class Ebook:
    """Represents an e-book in the catalog."""

    def __init__(self, title, author, publication_date, genre, price):
        """Initialize e-book details."""
        self.__title = title
        self.__author = author
        self.__publication_date = publication_date
        self.__genre = genre
        self.__price = price

    # Getters and setters for each attribute
    def get_title(self):
        return self.__title

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        self.__price = new_price

    def __str__(self):
        """Returns a string representation of the e-book."""
        return f"{self.__title} by {self.__author}, {self.__genre} - ${self.__price:.2f}"
