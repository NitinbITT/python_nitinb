def fibonacci(number_of_fibonacci):
    current = 1
    previous = 0
    if number_of_fibonacci == 1:
        yield previous
        return
    yield previous
    yield current
    for _ in range(number_of_fibonacci - 2):
        yield current + previous
        current = current + previous
        previous = current - previous


try:
    number_of_fibonacci = int(input("Enter Number of Fibonacci: "))
    if number_of_fibonacci <= 0:
        print("invalid number")
    else:
        numbers = fibonacci(number_of_fibonacci)
        for number in numbers:
            print(number)
except ValueError as e:
    print(e, "Enter a number")
