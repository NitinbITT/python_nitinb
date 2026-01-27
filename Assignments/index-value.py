def index_value(number_list):
    index_value = []
    for index in range(len(number_list)):
        index_value.append((index, number_list[index]))
    return index_value


number_list = list(map(int, input("Enter the numbers ").split()))
print(index_value(number_list))
