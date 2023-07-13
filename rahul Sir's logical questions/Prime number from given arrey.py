# prime number from given arrey:- 

A = [23,2,30,4,56,78,1,5,6,7,90,6,4]

prime = []

for i in A:
    c=0
    for j in range(2,n+1):
        if i%j==0:
            c+=1
    if c==1:
        prime.append(i)
print(prime)
