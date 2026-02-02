class Account:
    def __init__(self,accno,ifsc,name):
        self.__accno=accno
        self.__ifsc=ifsc
        self.__name=name
    
    def getAccno(self):
        return self.__accno

    def getIFSC(self):
        return self.__ifsc
    
    def getUname(self):
        return self.__name


class DMATaccount(Account):
    def __init__(self,accno,ifsc,name,dmatamount):
        super().__init__(accno,ifsc,name)
        self.dmatamount=dmatamount
    
    def action(self):
        print("This is from DMAT account")

class SavingsAccount(Account):
    def __init__(self,accno,ifsc,name,savingsamount):
        super().__init__(accno,ifsc,name)
    
    def action(self):
        print("This is from Savings account")


s=SavingsAccount("acc123","bank1321","name1",9000)
d=DMATaccount("acc122","bank1322","name2",9000)
a=Account("acc121","bank1323","name3")

s.action()
print(s.getUname())
d.action()
print(d.getUname())

print(a.__accno)