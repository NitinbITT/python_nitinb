from enum import Enum


class Mode(Enum):
    OFF = 0
    HEATING = 1
    COOLING = 2


class Thermostat:
    def __init__(self, current):
        self._current_temperature = current
        self._target_temperature = current
        self._mode = Mode.OFF

    def set_target_temperature(self, target_temperature):
        self._target_temperature = target_temperature
        self.set_mode()

    def set_mode(self):
        if self._current_temperature > self._target_temperature:
            self._mode = Mode.COOLING
        elif self._current_temperature < self._target_temperature:
            self._mode = Mode.HEATING
        else:
            self._mode = Mode.OFF

    def get_mode(self):
        return self._mode.name


try:
    current_temperature = int(input("Enter current temperature: "))
    target_temperature = int(input("Enter target temperature: "))
    smart_thermostat = Thermostat(current_temperature)
    smart_thermostat.set_target_temperature(target_temperature)
    print("Mode:", smart_thermostat.get_mode())
except ValueError as e:
    print(e, "Enter a valid number")
