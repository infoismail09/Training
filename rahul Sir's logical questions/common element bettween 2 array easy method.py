# common element bettween 2 array

a=[4, 5, 6, 7, 8, 9]
b=[11, 12, 13, 6, 7, 8, 9]


commons=[]

for i in a:
    if i in b:
        commons.append(i)
print(commons)
