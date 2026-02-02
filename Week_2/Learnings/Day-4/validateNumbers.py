from validateWrapper import Validate

class SampleClass:
    def __init__(self, number):
        self.number = number
        self.validator = Validate(number) 

    def checkValidation(self):
        if self.validator.checkPositive() and self.validator.checkOdd():
            return "Number is positive and odd"
        return "Validation failed"

sample=SampleClass(5)

sample.checkValidation()