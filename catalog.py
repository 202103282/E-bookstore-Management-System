from ebook import Ebook

class Catalog:
    """Manages a collection of ebooks with functionalities to add, remove, and search."""

    def __init__(self):
        self._ebooks = []

    def add_ebook(self, ebook: Ebook):
        """Adds an ebook to the catalog."""
        self._ebooks.append(ebook)

    def remove_ebook(self, ebook: Ebook):
        """Removes an ebook from the catalog."""
        self._ebooks.remove(ebook)

    def search_ebook(self, criteria: str):
        """Searches for ebooks that match the criteria in title, author, or genre."""
        return [ebook for ebook in self._ebooks if criteria.lower() in (ebook.title.lower() + ebook.author.lower() + ebook.genre.lower())]

    def __str__(self):
        return f"Catalog({len(self._ebooks)} ebooks)"
