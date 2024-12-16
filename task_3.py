class Library:
    book_list = []

    def entry_book(self,book):
        self.book_list.append(book)



class Book:
    def __init__(self, book_id, title, author, availability):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.availability = availability
        
        
    def __repr__(self):
        return f'(Bookid:{self.book_id}, title:{self.title}, author:{self.author}, available:{self.availability})'
    
     
lib = Library()
B1 = Book(101, 'harrypotter','harry', True)
B2 = Book(102, 'harrtter','jerry', False)

lib.entry_book(B1)
lib.entry_book(B2)


print('booklist: ', Library.book_list)