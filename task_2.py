class Book:
    def __init__(self, book_id, title, author, availability):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.availability = availability

    def __repr__(self):
        return f'(Bookid:{self.book_id}, title:{self.title}, author:{self.author}, available:{self.availability})'
    
     
harry = Book(101, 'HarryPotter', 'Harry', True)
jerry = Book(102, 'HarryPotter', 'Jerry', False)
print(harry)
print(jerry)


