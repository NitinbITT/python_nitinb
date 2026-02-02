def evaluate_number(number):
    sum = 0
    for string_digit in str(number):
        sum += int(string_digit) ** 2
    return sum


def is_happy(number):
    seen = set()
    while number != 1:
        if number in seen:
            return False
        seen.add(number)
        number = evaluate_number(number)
    return True


def next_happy_number(number):
    number = number + 1
    while True:
        if is_happy(number):
            yield number
        number += 1


try:
    number = int(input("Enter a number:"))
    happy_numbers = next_happy_number(number)
    print(next(happy_numbers))
except ValueError as e:
    print(e, "Enter a number")
