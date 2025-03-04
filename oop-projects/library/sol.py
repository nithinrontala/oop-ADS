import uuid

class Book:
    def __init__(self,sub,name,id):
        self.title = sub
        self.author = name
        self.id = id
        self.is_available = True

class User:
    def __init__(self,name):
        self.name = name
        self.user_id = str(uuid.uuid4())
        self.borrowed_books = []
        self.borrowing_history = []
    
    def borrow_book(self,book):
        if book.is_available == True:
            book.is_available = False
            self.borrowed_books.append(book) 
            self.borrowing_history.append((book, "Borrowed"))
            return f"{self.name} borrowed '{book.title}'"
        return "Book is not available"
    
    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_available = True
            self.borrowed_books.remove(book)
            self.borrowing_history.append((book, "Returned"))
            return f"{self.name} returned '{book.title}'"
        return "Book was not borrowed"
    
class Library:
    def __init__(self, name):
        self.name = name
        self.books = {}
        self.users = {}
    
    def add_book(self, book):
        self.books[book.id] = book
    
    def register_user(self, user):
        self.users[user.user_id] = user
    
    def search_book(self, query):
        r = []
        query = query.lower()  
        for book in self.books.values():
            if query in book.title.lower() or query in book.author.lower():
                r.append(book)
        return r

    
    def borrow_book(self, user, book):
        return user.borrow_book(book)
    
    def return_book(self, user, book):
        return user.return_book(book)
    
    def __str__(self):
        return f"Library: {self.name} | Total Books: {len(self.books)} | Total Users: {len(self.users)}"

if __name__ == "__main__":
    library = Library("SmartLibrary")
    
    book1 = Book("Python Programming", "John Doe", "12345")
    book2 = Book("Object-Oriented Design", "Jane Smith", "67890")
    
    user1 = User("Alice")
    user2 = User("Bob")
    
    library.add_book(book1)
    library.add_book(book2)
    library.register_user(user1)
    library.register_user(user2)
    
    print(library.borrow_book(user1, book1))
    print(library.borrow_book(user2, book1))  # Should be unavailable
    print(library.return_book(user1, book1))
    print(library.borrow_book(user2, book1))  # Now available
    
    print("\nLibrary Status:")
    print(library)