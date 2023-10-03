import math

class Book:
    def __init__(self, id, title, author, price, rating):
        self._id = id
        self._title = title
        self._author = author
        self._price = price
        self._rating = rating

    def book_info(self):
        print(f"{self._id}\n{self._title}\n{self._author}\n{self._price}\n{self._rating}")


class Booklist:
    def __init__(self):
        self._books = []

    def add_book(self,book):
        self._books.append(book)
    
    def show_books(self):
        for book in self._books:
            print(book)
            print("\n")


    def find_book_by_id(self, bookid):
        for book in self._books:
            if book._id == bookid:
                return book
            else:
                return None
            


    def all_books_by_author(self, author):
        books =[]
        for book in self._books:
            if book._author == author:
                books.append(book)

        return books


    def find_books_in_rating_range(self, min_range, max_range):
        books =[]
        for book in self._books:
            if min_range <= book._rating <= max_range:
                books.append(book)

        return books

    def find_books_in_price_range(self, min_price, max_price):
        books =[]
        for book in self._books:
            if min_price <= book._price <= max_price:
                books.append(book)

        return books

        

Booklist1 = Booklist()

b1 = Book(1, "Book1", "Author1", 100, 4.5)
b2 = Book(2, "Book2", "Author2", 120, 4.6)
b3 = Book(3, "Book3", "Author3", 160, 4.8)
b4 = Book(4, "Book4", "Author1", 200, 4.7)

Booklist1.add_book(b1)
Booklist1.add_book(b2)
Booklist1.add_book(b3)
Booklist1.add_book(b4)

#Booklist1.show_books()

temp = Booklist1.find_book_by_id(1)
temp.book_info()


min_price =50
max_price = 150
bl1 = Booklist1.find_books_in_price_range(min_price, max_price)
print(f"\n Books in price range {min_price}, {max_price}:")
print(len(bl1))
for book in bl1:
    book.book_info()
    print()

min_range = 4
max_range = 5
bl2 = Booklist1.find_books_in_rating_range(min_range,max_range)
print(f"\n Books in rating range {min_range}, {max_range}:")
print(len(bl2))
for book in bl2:
    book.book_info()
    print()

author1 = 'Author1'
bl3 = Booklist1.all_books_by_author(author1)

print(f"\n Books by author {author1}:")
for book in bl3:
    book.book_info()
    print()




