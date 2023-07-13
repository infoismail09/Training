# 80, 60, 10, 50, 30, 100, 0, 50]
# Find pairs whose sum = 100;
# Logic for above problem?
# What will be the complexity for it?
# Any better solution for the above problem?

a = [80, 60, 10, 50, 30, 100, 0, 50]

pairs=[]

for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]+a[j]==100:
            pairs.append((a[i],a[j]))
            
print(pairs)
