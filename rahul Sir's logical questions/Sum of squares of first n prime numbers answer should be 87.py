# 18. Sum of squares of first n prime numbers
# Input = 4, Answer = 87
# Explanation: 2*2+3*3+5*5+7*7 = 87


n=int(input("Enter the Number"))

counter=0

for i in range(2,n+1):
    c=0
    for j in range(2,int(i/2)):
        if (i%j==0):
            c=1
            break
    if (c==0):
        print(i,end=' ')
        counter = counter+i**2
print("\nprime square addition",counter)
