class LibraryItem:
    def __init__(self, name):
        self.__name = name
        self.__availability = True

    def get_name(self):
        return self.__name

    def is_available(self):
        return self.__availability

    def put_availability(self, availability):
        self.__availability = availability
