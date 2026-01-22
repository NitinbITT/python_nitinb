numberList1 = [1, 2, 3, 2, 1, 3, 4, 5, 1, 5, 3, 4, 2]
numberList2 = []

for number in numberList1:
    if number not in numberList2:
        numberList2.append(number)

print("Unique Number List:", numberList2)
