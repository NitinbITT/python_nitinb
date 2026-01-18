prime=[
    i
    for i in range(2,11)
    if sum(1 for j in range(1,i+1) if i%j==0)==2
]

print(prime)