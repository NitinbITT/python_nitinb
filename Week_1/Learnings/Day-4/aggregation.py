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
    
    def printDetails(self):
        self.acc.accDetails()

acc=Account("acc234","Alex",9000)
user=User(acc)

user.printDetails()
