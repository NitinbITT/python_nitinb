from abc import ABC, abstractmethod
class Account(ABC):
    def __init__(self,amount):
        self.amount=amount
    
    @abstractmethod
    def getamount(self):
        pass

class SavingsAccount(Account):
    def __init__(self,amount):
        super().__init__(amount)

    def anotherMethod(self):
        print("Another method")

    def getamount(self):
        print(amount)

s=SavingsAccount()
