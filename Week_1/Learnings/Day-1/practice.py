# from packages import module_calculations as cal

# print(__name__)

# print(cal.add(1,2))
# print(cal.sub(1,2))
# print(cal.mul(1,2))
# print(cal.div(1,2))

class InvalidValueException(Exception):
    pass

try:
    n=2
    if n<5:
        raise InvalidValueException("Value less than 5")
except InvalidValueException as e:
    print(e,"Exception")
else:
    print("Printing...")
finally:
    print("Success")