numberList1 = [1, 2, 3, 4, 5, 5]
numberList2 = [7, 6, 2, 3, 5, 8, 9]
numberList3 = []
for number in numberList1:
    if number in numberList2:
        numberList3.append(number)

print("Common Values in the lists:", set(numberList3))
