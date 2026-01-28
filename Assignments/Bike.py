from Engine import Engine


class Bike:
    def __init__(self):
        self.__engine = Engine()

    def start_bike(self):
        if self.__engine.start():
            return True
        else:
            return False

    def ride_bike(self):
        if self.__engine.run():
            return True
        else:
            return False

    def stop_bike(self):
        if self.__engine.stop():
            return True
        else:
            return False


new_bike = Bike()

if new_bike.start_bike():
    print("Bike Started")
if new_bike.ride_bike():
    print("Bike riding")
if new_bike.stop_bike():
    print("Bike stopped")
