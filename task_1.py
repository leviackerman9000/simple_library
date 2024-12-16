class Book:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def __repr__(self):
        return f'(Book:{self.name}, id:{self.id})'

class Library:
    book_list = []

    def entry_book(self, book):
        self.book_list.append(book)


mylibrary = Library()

B1 = Book('harry',101)
B2 = Book('jerry',102)
mylibrary.entry_book(B1)
mylibrary.entry_book(B2)

print(mylibrary.book_list)

