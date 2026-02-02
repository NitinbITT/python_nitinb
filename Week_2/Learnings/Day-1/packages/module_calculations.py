def add(a,b):
    return a+b
def sub(a,b):
    if a>=b:
        return a-b
    else:
        return b-a

def mul(a,b):
    return a*b

def div(a,b):
    if a==0:
        return 0
    return a/b

print(__name__)