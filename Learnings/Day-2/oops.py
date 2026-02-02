class User:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def displayDetails(self):
        print("Generic user",self.name,self.age)

    def action(self):
        print("Performs all action")

class Admin(User):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def displayDetails(self):
        super().action()
        print("Details of admin:",self.name,self.age)

generic=User("Gen",13)
generic.displayDetails()

admin=Admin("Alex",12)
admin.displayDetails()
