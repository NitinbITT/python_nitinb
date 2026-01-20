class User:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def printDetails(self):
        # print(self.name,self.age)
        print("hello")
    
u=User("Alex",12)
u.printDetails()