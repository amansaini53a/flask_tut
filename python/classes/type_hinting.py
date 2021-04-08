from typing import List


def list_average(sequence: List) -> float:
    return sum(sequence) / len(sequence)


class Book:
    pass


class Bookshelf:
    def __init__(self, books: List[Book]):
        self.books = books

    def __str__(self) -> str:
        return f"Bookshelf with {len(self.books)} books."
