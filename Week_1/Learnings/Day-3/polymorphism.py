class Account:
    def __init__(self,accno,ifsc,name):
        self.accno=accno
        self.ifsc=ifsc
        self.name=name
    
    def getAccno(self):
        return self.accno

    def getIFSC(self):
        return self.accno
    
    def getUname(self):
        return self.name


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

s.action()
print(s.getUname())
d.action()
print(d.getUname())