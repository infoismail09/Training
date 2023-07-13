# frequency of a string

putin = 'Engineeer'

A={}
for i in putin:
        if i in A:
            A[i]+=1
        else:
            A[i]=1
print(A)
