# WAP with 2 different logic, to find all duplicate number in an array

# 1 way) 

arr = [80, 60, 10, 50, 30, 100, 0, 50];    

for i in range(0, len(arr)):  
    for j in range(i+1, len(arr)):  
        if(arr[i] == arr[j]):  
            print("Duplicate elements in given array : ",arr[j])

# print("Duplicate elements in given array: ",arr);



2nd way:-

#with 2 different logic, to find all duplicate number in an array

lis = [1, 2, 1, 2, '3', 4, 5, '3', 1, 2, 5, 6, 7, 8, 9, 9]
x = []
y = []
for i in lis:
    if i not in x:
        x.append(i)
for i in x:
    if lis.count(i) > 1:
        y.append(i)
print(y)
