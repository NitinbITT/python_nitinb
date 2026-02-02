class ReverseIterate:
    def __init__(self, number_list):
        self.number_list = number_list
        self.start = len(number_list) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < 0:
            raise StopIteration
        index = self.start
        self.start = self.start - 1
        return self.number_list[index]


try:
    number_list = list(map(int, input("Enter numbers: ").split(" ")))
    iterator = ReverseIterate(number_list)
    print("Iterating in reverse: ", end="")
    for index in iterator:
        print(index, end=" ")
except ValueError as e:
    print(e, "\nEnter a number !!")
