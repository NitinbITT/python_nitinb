def decimalToOctal(decimal):
    rem = 0
    digit = 1
    octal = 0
    while decimal > 0:
        rem = decimal % 8
        decimal //= 8
        octal += digit * rem
        digit *= 10
    return "0o" + str(octal)


def octalToDecimal(octal):
    power = len(octal) - 3
    print(power)
    decimal = 0
    index = 2
    while power >= 0:
        decimal += (int(octal[index])) * (8**power)
        index += 1
        power -= 1
    return decimal


decimal_number = 125

octal_number = decimalToOctal(decimal_number)
decimal_number = octalToDecimal(octal_number)

print("Decimal to octal:", octal_number, "| Octal to Decimal:", decimal_number)
