class Book():
    def __init__(self, title, author, isbn, copies_available):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies_available = copies_available

    def __str__(self):
        return f"Book - Title: '{self.title} || Author: '{self.author} || ISBN: '{self.isbn} || Copies Available '{self.copies_available}"


    def borrow_book(self):
        if  self.copies_available >= 1:
            self.copies_available -= 1
            print(f"You have borrowed the Book titled '{self.title}'. Enjoy!")
        else:
            print(f"Book titled '{self.title}' is not available for borrowing, Try again later!")
    

    def return_book(self):
        self.copies_available += 1
        print(f"You have returned the Book titled '{self.title}'. See you again!")

class Person():
    def __init__(self, name):
        self.name = name


class Member(Person):
    def __init__(self, name, member_id):
        super().__init__(name)
        self.member_id = member_id
        self.borrowed_books = []

    def __str__(self):
        return f"Member - Name: '{self.name} || Memeber ID: '{self.member_id} || Borrowed Books: '{self.borrowed_books}"
    
    def books_borrowed(self, book):
        self.borrowed_books.append(book)
        print(f"{book.title} has been added to your borrowed list")

    def books_returned(self, book):
        self.borrowed_books.remove(book)
        print(f"{book.title} has been removed to your borrowed list")


book1 = Book("book1", "author1", "11111", 1)
book2 = Book("book2", "author2", "22222", 2)
book3 = Book("book3", "author3", "33333", 3)
book4 = Book("book4", "author4", "44444", 4)
print(book1)

book1.borrow_book()
book1.return_book()


m1 = Member("member1", "01")
m2 = Member("member2", "02")
m3 = Member("member3", "03")
m4 = Member("member4", "04")
m5 = Member("member5", "05")

m1.books_borrowed(book1)
m1.books_borrowed(book2)
m1.books_borrowed(book3)
print(m1)


m1.books_returned(book3)
print(m1)