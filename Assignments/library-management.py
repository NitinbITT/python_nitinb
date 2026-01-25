class Book:
    def __init__(self, name, author):
        self.__name = name
        self.__author = author
        self.__availability = True

    def get_book_name(self):
        return self.__name

    def get_book_availability(self):
        return self.__availability

    def get_book_author(self):
        return self.__author

    def put_book_availability(self, availability):
        self.__availability = availability

    def __str__(self):
        return f"Name: {self.__name}  Author: {self.__author}  Availability: {self.__availability}"


class Library:
    def __init__(self, name, address):
        self.__name = name
        self.__address = address
        self.__book_list = []

    def display_library_details(self):
        print("Library Details")
        print("Name:", self.__name, " Address:", self.__address)

    def display_all_books(self):
        for book in self.__book_list:
            print(book)

    def add_book(self, name, author):
        for book in self.__book_list:
            if name.strip().lower() == book.get_book_name().strip().lower():
                print("Book already exists")
                return
        self.__book_list.append(Book(name, author))
        print("Book added successfully")

    def lend_book(self, book_name):
        for book in self.__book_list:
            if book_name.strip().lower() == book.get_book_name().strip().lower():
                if book.get_book_availability():
                    book.put_book_availability(False)
                    print("Book lent successfully")
                else:
                    print("Book not available at the moment")
                return
        print("Book not found")

    def receive_book(self, book_name):
        for book in self.__book_list:
            if book_name.strip().lower() == book.get_book_name().strip().lower():
                book.put_book_availability(True)
                print("Book received successfully")
                return
        print("Book not found")


def add_book_menu(library):
    print("----- Add Book -----")
    name = input("Enter Book Name: ")
    author = input("Enter Author Name: ")
    library.add_book(name, author)


def lend_book_menu(library):
    print("----- Lending Book -----")
    book_name = input("Enter Book Name: ")
    library.lend_book(book_name)


def receive_book_menu(library):
    print("----- Receiving Book -----")
    book_name = input("Enter Book Name: ")
    library.receive_book(book_name)


def library_management():
    library = Library("ABC_Library", "Address.....")

    while True:
        print("\n1. Add book")
        print("2. Lend book")
        print("3. Receive book")
        print("4. Display book")
        print("5. Exit")

        option = int(input("Enter an option: "))

        match option:
            case 1:
                add_book_menu(library)
            case 2:
                lend_book_menu(library)
            case 3:
                receive_book_menu(library)
            case 4:
                library.display_all_books()
            case 5:
                return


library_management()
