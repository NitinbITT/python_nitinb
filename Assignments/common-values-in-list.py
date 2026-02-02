number_list_first = [1, 2, 3, 4, 5, 5]
number_list_second = [7, 6, 2, 3, 5, 8, 9]
number_list_third = []
for number in number_list_first:
    if number in number_list_second:
        number_list_third.append(number)

print("Common Values in the lists:", set(number_list_third))
