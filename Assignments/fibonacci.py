def fibonacci(number_of_fibonacci):
    i = 0
    current = 1
    previous = 0
    yield previous
    yield current
    while i < number_of_fibonacci - 2:
        yield current + previous
        current = current + previous
        previous = current - previous
        i += 1


number = fibonacci(5)
try:
    while True:
        print(next(number))
except:
    print("Completed Fibonacci series generation")
