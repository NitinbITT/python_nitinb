a=[1,2,3,2,1,3,4,5,1,5,3,4,2]
b=[]

for i in a:
    if i not in b:
        b.append(i)

print(b)