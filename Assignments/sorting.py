a=[7,4,6,2,8,1,5,3,9]

for i in range(len(a)):
    min_index=i
    min=a[i]
    for j in range(i+1,len(a)):
        if a[j] < min:
            min=a[j]
            min_index=j
    temp=a[i]
    a[i]=min
    a[min_index]=temp

print("After sorting List:",a)

dictionary={
    "name":"Alex",
    "age":12,
    "height":4.5,
    "weight":30
}


keys=list(dictionary.keys())
values=list(dictionary.values())

for i in range(len(keys)):
    for j in range(len(keys)):
        if keys[i] < keys[j] :
            temp=keys[i]
            keys[i]=keys[j]
            keys[j]=temp
            
            temp=values[i]
            values[i]=values[j]
            values[j]=temp
dictionary={}
for i in range(len(keys)):
    dictionary[keys[i]]=values[i]

print("After sorting dictionary:",dictionary)