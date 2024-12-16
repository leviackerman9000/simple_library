class Library:
    book_list = []

    def entry_book(self,book):
        self.book_list.append(book)

    # def view_all_books(self):

class Book:
    def __init__(self, book_id, title, author, availability):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.availability = availability

    def borrow_book(self):
        if self.availability == True:
            print('Book available')
            self.availability = False
        else:
            print('Book unavailable')
        
    def return_book(self):
        self.availability = True

    def view_book_info(self):
        print(f'Book_id:{self.book_id}, title:{self.title}, author:{self.author}, availability:{self.availability}') 
            

    def __repr__(self):
        return f'Bookid:{self.book_id}, title:{self.title}, author:{self.author}, available:{self.availability}\n'
    
     
lib = Library()
B1 = Book(101, 'harrypotter','harry', True)
B2 = Book(102, 'harrtter','jerry', False)
B3 = Book(103, 'harrtter','carrry', False)

lib.entry_book(B1)
lib.entry_book(B2)
lib.entry_book(B3)

B2.return_book()

# B1.view_book_info()
# B2.view_book_info()

print(lib.book_list)
