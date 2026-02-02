# a=[1,2,3]
# for i in a:
#     print(i)

# a=(1,2,3)
# a.append(5)
# for i in a:
#     print(i)

# a={1,2,3,3,3,2,2,2,2,2,2}
# print(a)
# a.add(5)
# a.remove(2)
# for i in a:
#     print(i)

# list1=[1,3,4,2,3,4,1,2,3]
# a=frozenset(list1)
# if 1 in a:
#     print(a)
# a.add(7)
# print(a)


# a=10
# b=2.5
# c=a+b                 # Implicit type conversion
# print(c)

# a=1.5
# b=int(a)                # Explicit type conversion
# print(b)
# boolean="true"
# print(type(boolean))
# print((bool(type(boolean))))

# a="101"
# b=int(a,2)
# print(b)

# # a=[]
# for i in range(6):
#     a.append(i)
# print(a)
# a.append(1)
# a.pop(1)
# print(a)

# a=[[]]
# for i in range(6):
#     b=[]
#     for j in range(6):
#         b.append(i+j)
#     a.append(b)

# print(a)

import numpy as np

# a=np.array([1,2,3])
# print(a)
# print(type(a))

# a=list(map(int,input("Enter values :").split(" ")))
# a=np.array(a)
# print(a)

a={
    "name":"Ankit",
    "age":12
}
for key in a:
    print(key,":",a[key])