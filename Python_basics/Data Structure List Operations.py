# List operatins:-

#1) Shifting all zero to the last



arr = [4,0,55,0,6,100,0,7,0,0,8,12,0,14]

NonZeroValues = [x for x in arr if x !=0]

zerovalues = [j for j in arr if j == 0 ]

result = NonZeroValues+zerovalues


#2)Highest lowest element

list = [3, 5, 5, 1, -5]

min(list)

max(list)

#0R

number = [3,4,5,6,7,9,0]

print(sorted(number,reverse=True))


#3)3rd highest eliment using min,max function an element

arr = [4,0,55,0,6,100,0,7,0,0,8,12,0,14]

print("3rd largest in",arr,"is",sorted(arr)[-3])
