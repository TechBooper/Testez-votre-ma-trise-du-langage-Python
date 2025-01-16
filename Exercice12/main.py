class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

class Library:
    def __init__(self):
        self.books = []
        self.borrowed_books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book_title):
        self.books = [book for book in self.books if book.title != book_title]

    def borrow_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                self.borrowed_books.append(book)
                print(f"Vous avez emprunté: {book.title}")
                return
        print("Livre non disponible.")

    def return_book(self, book_title):
        for book in self.borrowed_books:
            if book.title == book_title:
                self.borrowed_books.remove(book)
                self.books.append(book)
                print(f"Vous avez rendu: {book.title}")
                return
        print("Livre non emprunté.")

    def available_books(self):
        return [book.title for book in self.books]

    def borrowed_books_list(self):
        return [book.title for book in self.borrowed_books]

# Example usage
library = Library()
book1 = Book("1984", "George Orwell", 1949)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)

library.add_book(book1)
library.add_book(book2)

print("Livres disponibles:", library.available_books())
library.borrow_book("1984")
print("Livres disponibles après emprunt:", library.available_books())
library.return_book("1984")
print("Livres disponibles après retour:", library.available_books())
