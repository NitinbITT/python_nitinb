def evaluate_number(number):
    sumOfSquareDigits = 0
    for string_digit in str(number):
        sumOfSquareDigits += int(string_digit) ** 2
    return sumOfSquareDigits


def is_happy(number):
    seen = set()
    while number != 1:
        if number in seen:
            return False
        seen.add(number)
        number = evaluate_number(number)
    return True


def generate_happy_number(number):
    number += 1
    while True:
        if is_happy(number):
            yield number
        number += 1


try:
    number = int(input("Enter a number:"))
    happy_numbers = generate_happy_number(number)
    print(next(happy_numbers))
except ValueError as e:
    print(e, "Invalid input. Enter a number !!")
