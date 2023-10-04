class Book:
    def __init__(self, id, title, author, price, rating):
        self._id = id
        self._title = title
        self._author = author
        self._price = price
        self._rating = rating
        self._next = None

    def book_info(self):
        print(f"ID: {self._id}\nTitle: {self._title}\nAuthor: {self._author}\nPrice: {self._price}\nRating: {self._rating}\n")


class BookLinkedList:
    def __init__(self):
        self._first = None

    def add_book(self, book):
        if self._first is None:
            self._first = book
        else:
            current = self._first
            while current._next:
                current = current._next
            current._next = book

    def show_books(self):
        current = self._first
        while current:
            current.book_info()
            current = current._next

    def find_book_by_id(self, bookid):
        current = self._first
        while current:
            if current._id == bookid:
                return current
            current = current._next

        return None

    def all_books_by_author(self, author):
        books = []
        current = self._first
        while current:
            if current._author == author:
                books.append(current)
            current = current._next

        return books

    def find_books_in_rating_range(self, min_range, max_range):
        books = []
        current = self._first
        while current:
            if min_range <= current._rating <= max_range:
                books.append(current)
            current = current._next

        return books

    def find_books_in_price_range(self, min_price, max_price):
        books = []
        current = self._first
        while current:
            if min_price <= current._price <= max_price:
                books.append(current)
            current = current._next

        return books

Booklist1 = BookLinkedList()

b1 = Book(1, "Book1", "Author1", 100, 4.5)
b2 = Book(2, "Book2", "Author2", 120, 4.6)
b3 = Book(3, "Book3", "Author3", 160, 4.8)
b4 = Book(4, "Book4", "Author1", 200, 4.7)

Booklist1.add_book(b1)
Booklist1.add_book(b2)
Booklist1.add_book(b3)
Booklist1.add_book(b4)

print("All Books:")
Booklist1.show_books()


min_price = 50
max_price = 150
bl1 = Booklist1.find_books_in_price_range(min_price, max_price)
print(f"\n Books in price range {min_price}, {max_price}:")
for book in bl1:
    book.book_info()


min_range = 4
max_range = 5
bl2 = Booklist1.find_books_in_rating_range(min_range,max_range)
print(f"\n Books in rating range {min_range}, {max_range}:")
for book in bl2:
    book.book_info()


author1 = 'Author1'
print(f"\nBooks by Author: {author1}:")
bl3 = Booklist1.all_books_by_author("Author1")
for book in bl3:
    book.book_info()


print("\nFind Book by ID:")
b = Booklist1.find_book_by_id(2)
if b:
    b.book_info()
else:
    print("Book not found.")



