def index_value(numberList):
    index_value = []
    for index in range(len(numberList)):
        index_value.append((index, numberList[index]))
    return index_value


numberList = list(map(int, input("Enter the numbers ").split()))
print(index_value(numberList))
