def index_value(list1):
    return [(i,list1[i]) for i in range(len(list1))]
    
list1=list(map(int,input("Enter the numbers ").split()))
print(index_value(list1))