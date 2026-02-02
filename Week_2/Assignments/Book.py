from LibraryItem import LibraryItem


class Book(LibraryItem):
    def __init__(self, name, author):
        super().__init__(name)
        self.__author = author

    def get_author(self):
        return self.__author

    def __str__(self):
        return f"Name: {super().get_name()}  Author: {self.__author}  Availability: {super().is_available()}"
