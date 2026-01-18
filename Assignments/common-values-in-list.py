a=[1,2,3,4,5]
b=[7,6,2,3,5,8,9]
c=[]
for i in a:
    if i in b:
        c.append(i)

print(c)