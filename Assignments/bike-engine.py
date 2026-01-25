class Engine:
    def __init__(self, cc, torque):
        self.cc = cc
        self.torque = torque

    def start(self):
        print("Engine started", end=" - ")

    def run(self):
        print("Engine running", end=" - ")

    def stop(self):
        print("Engine stopped", end=" - ")


class Bike:
    def __init__(self, engine):
        self.engine = engine

    def start_bike(self):
        self.engine.start()
        print("Bike Started")

    def ride_bike(self):
        self.engine.run()
        print("Bike riding")

    def stop_bike(self):
        self.engine.stop()
        print("Bike stopped")


engine = Engine(450, 100)
new_bike = Bike(engine)

new_bike.start_bike()
new_bike.ride_bike()
new_bike.stop_bike()
