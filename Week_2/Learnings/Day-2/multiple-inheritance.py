class A:
    def printing(self):
        print("Printing from Class A")


        
class B(A):
    def printing(self):
        print("Printing from Class B")
class C(A):
    def printing(self):
        print("Printing from Class C")
class D(B,C):
    def printinganother(self):
        print("Printing from Class D")

d=D()
d.printing()