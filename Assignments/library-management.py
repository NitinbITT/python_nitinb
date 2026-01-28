from Book import Book


class Library:
    def __init__(self, name, address):
        self.__name = name
        self.__address = address
        self.__book_list = []

    def get_all_books(self):
        return self.__book_list

    def is_book_present(self, book_name):
        for book in self.__book_list:
            if book_name.strip().lower() == book.get_name().strip().lower():
                return book
        return None

    def add_book(self, name, author):
        if self.is_book_present(name):
            return False
        self.__book_list.append(Book(name, author))
        return True

    def lend_book(self, book_name):
        book = self.is_book_present(book_name)
        if book:
            if book.is_available():
                book.put_availability(False)
                return True
            else:
                return False

    def receive_book(self, book_name):
        book = self.is_book_present(book_name)
        if book:
            if not book.is_available():
                book.put_availability(True)
                return True
            else:
                return False


def add_book_menu(library):
    print("----- Add Book -----")
    name = input("Enter Book Name: ")
    author = input("Enter Author Name: ")
    if library.add_book(name, author):
        print("Book added successfully")
    else:
        print("Cannot add book")


def lend_book_menu(library):
    print("----- Lending Book -----")
    book_name = input("Enter Book Name: ")
    if library.lend_book(book_name):
        print("Book lent successfully")
    else:
        print("Cannot Lend Book")


def receive_book_menu(library):
    print("----- Receiving Book -----")
    book_name = input("Enter Book Name: ")
    if library.receive_book(book_name):
        print("Book received successfully")
    else:
        print("Cannot recieve Book")


def display_all_books(library):
    books = library.get_all_books()
    for book in books:
        print(book)


def library_management():
    library = Library("ABC_Library", "Address.....")

    while True:
        print("\n1. Add book")
        print("2. Lend book")
        print("3. Receive book")
        print("4. Display book")
        print("5. Exit")

        try:
            option = int(input("Enter an option: "))
            match option:
                case 1:
                    add_book_menu(library)
                case 2:
                    lend_book_menu(library)
                case 3:
                    receive_book_menu(library)
                case 4:
                    display_all_books(library)
                case 5:
                    return
                case _:
                    print("Enter valid option")
        except ValueError as e:
            print(e, "Enter a number")


library_management()
