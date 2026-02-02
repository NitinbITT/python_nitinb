class Bank:
    def __init__(self, name, ifsc):
        self.name=name
        self.ifsc=ifsc
    
    def printBankDetails(self):
        print(self.name,self.ifsc)

class Account:
    def __init__(self,accno,name,amount):
        self.accno=accno
        self.name=name
        self.amount=amount
    
    def accDetails(self):
        print(self.accno,self.name,self.amount)

class User:
    def __init__(self,acc):
        self.acc=acc

    def printDetails(self,bank):
        self.acc.accDetails()
        bank.printBankDetails()

bank = Bank("Bank1", "IFSC1155")
acc=Account("acc001", "Alex", 8000)
user = User(acc)

user.printDetails(bank)
