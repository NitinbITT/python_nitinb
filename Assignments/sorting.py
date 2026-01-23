def sort_list(numbers):
    for i_index in range(len(numbers)):
        min_index = i_index
        minimum = numbers[i_index]
        for j_index in range(i_index + 1, len(numbers)):
            if numbers[j_index] < minimum:
                minimum = numbers[j_index]
                min_index = j_index
        temp = numbers[i_index]
        numbers[i_index] = minimum
        numbers[min_index] = temp


def sort_dictionary(dictionary):
    keys = list(dictionary.keys())
    values = list(dictionary.values())

    for i_index in range(len(keys)):
        for j_index in range(len(keys)):
            if keys[i_index] < keys[j_index]:
                temp = keys[i_index]
                keys[i_index] = keys[j_index]
                keys[j_index] = temp

                temp = values[i_index]
                values[i_index] = values[j_index]
                values[j_index] = temp
    dictionary = {}
    for index in range(len(keys)):
        dictionary[keys[index]] = values[index]
    return dictionary


numbers = [7, 4, 6, 2, 8, 1, 5, 3, 9]
dictionary = {"name": "Alex", "age": 12, "height": 4.5, "weight": 30}
sort_list(numbers)
dictionary = sort_dictionary(dictionary)
print("After sorting List:", numbers)
print("After sorting dictionary:", dictionary)
