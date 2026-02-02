number_list_first = [1, 2, 3, 2, 1, 3, 4, 5, 1, 5, 3, 4, 2]
number_list_second = []

for number in number_list_first:
    if number not in number_list_second:
        number_list_second.append(number)

print("Unique Number List:", number_list_second)
