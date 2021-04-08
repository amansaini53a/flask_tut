from typing import List

class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name : str, book_type : str, weight : int):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self) -> str:
        return f"<Book: {self.name}, Type: {self.book_type},Weight: {self.weight}>"

    @classmethod
    def hardcover(cls,name:str, page_weight:int) -> "Book":
        return cls(name, cls.TYPES[0], page_weight+100)

    @classmethod
    def paperweight(cls,name:str, page_weight:int) -> "Book":
        return cls(name,cls.TYPES[1], page_weight +100)
