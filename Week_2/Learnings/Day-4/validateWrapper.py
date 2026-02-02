class Validate:
    def __init__(self, number):
        self.number = number

    def checkPositive(self):
        return self.number > 0

    def checkOdd(self):
        return self.number % 2 != 0