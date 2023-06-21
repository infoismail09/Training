# Write a program to sum all the values of a dictionary.

marks = {"m1":12,"m2":23,"m3":5,"m4":6,"m5":9}

total=[]

for i in marks.values():
    total.append(i)
    
print("sum of values is :",sum(total))

