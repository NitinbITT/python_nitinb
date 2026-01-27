def decimal_to_octal(decimal):
    remainder = 0
    digit = 1
    octal = 0
    while decimal > 0:
        remainder = decimal % 8
        decimal //= 8
        octal += digit * remainder
        digit *= 10
    return "0o" + str(octal)


def octal_to_decimal(octal):
    power = len(octal) - 3
    decimal = 0
    index = 2
    while power >= 0:
        decimal += (int(octal[index])) * (8**power)
        index += 1
        power -= 1
    return decimal


decimal_number = 125

octal_number = decimal_to_octal(decimal_number)
decimal_number = octal_to_decimal(octal_number)

print("Decimal to octal:", octal_number, "| Octal to Decimal:", decimal_number)
