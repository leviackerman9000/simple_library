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

    def borrow_book(self):
        if self.availability == True:
            print('Book available')
            self.availability = False
        else:
            print('Book unavailable, has been already borrowed')
        
    def return_book(self):
        if self.availability == False:
            print('Thanks for returning the book.')
            self.availability = True
        else:
            print('This book has not been borrowed')
        
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

while True:
    print('\n   M E N U\n1. View All Books\n2. Borrow Book\n3. Return Book\n4. Exit')

    option = input('\nEnter an option: ')

    if option == '1':
        print(f'\nAll the books are: \n{lib.book_list}')

    elif option =='2':
        bookno = int(input('Enter book id to borrow: '))
        check = False
        for book in lib.book_list:
            if book.book_id == bookno:
                book.borrow_book()
                check = True
        if check == False:
            print('\nInvalid Book ID, provide a valid book ID')

    elif option == '3':
        bookno = int(input('Enter book id to return: '))
        check = False
        for book in lib.book_list:
            if book.book_id == bookno:
                book.return_book()
                check = True
        if check == False:
            print('\nInvalid Book ID, provide a valid book ID')

    elif option == '4':
        print('\nExiting the menu')
        break
    else:
        print('\nInvalid option !')
