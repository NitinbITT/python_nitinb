class reverse_iterate:
    def __init__(self, size, number_list):
        self.number_list = number_list
        self.start = size - 1
        self.end = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end:
            raise StopIteration
            return
        index = self.start
        self.start = self.start - 1
        return number_list[index]


number_list = list(map(int, input("Enter numbers: ").split(" ")))
iterator = reverse_iterate(len(number_list), number_list)
print("Iterating in reverse: ", end="")
for i in iterator:
    print(i, end=" ")
