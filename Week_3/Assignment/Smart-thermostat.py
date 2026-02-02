from enum import Enum


class Mode(Enum):
    OFF = 0
    HEATING = 1
    COOLING = 2


class Thermostat:
    def __init__(self, current, target):
        self.__current_temperature = current
        self.__target_temperature = target
        if self.__current_temperature > self.__target_temperature:
            self.__mode = Mode.COOLING
        elif self.__current_temperature < self.__target_temperature:
            self.__mode = Mode.HEATING
        else:
            self.__mode = Mode.OFF

    def get_mode(self):
        return self.__mode.name


try:
    current_temperature = int(input("Enter current temperature: "))
    target_temperature = int(input("Enter target temperature: "))
    smart_thermostat = Thermostat(current_temperature, target_temperature)
    print("Mode:", smart_thermostat.get_mode())
except ValueError as e:
    print(e, "Enter a valid number")
