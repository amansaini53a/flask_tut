# Add Functionality to the self.books
# Inheritance means a Book is a BookShelf
# Composition Bookshelf has Book many books



class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"BookShelf with {len(self.books)} books"


class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"


book = Book("Aman")
book2 = Book("Saini")
shelf = BookShelf(book2, book)
print(shelf)
