def generate_exponent(base, exponent_range):
    for exponent in range(0, exponent_range + 1):
        yield base**exponent


try:
    base = int(input("Enter the base number: "))
    exponent = int(input("Enter the exponent: "))
    exponent_generator = generate_exponent(base, exponent)
    for base_exponent in exponent_generator:
        print(base_exponent)
except ValueError as e:
    print(e, "Enter a number")
