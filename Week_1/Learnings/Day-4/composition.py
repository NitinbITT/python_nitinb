class Account:
    def __init__(self,accno,name,amount):
        self.accno=accno
        self.name=name
        self.amount=amount
    
    def printAccDetails(self):
        print(self.accno,self.name,self.amount)

class User:
    def createAccount(self,accno,name,amount):
        self.account=Account(accno,name,amount)
    
    def userDetails(self):
        self.account.printAccDetails()

user=User()

user.createAccount("acc231","Alex",6000)
user.userDetails()