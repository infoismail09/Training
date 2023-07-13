# shifting zeroes to the left,Right

arr = [5,6,0,4,0,2,0,3,7,0]


NonZeroes=[x for x in arr if x!=0]

Zeroes=[j for j in  arr if j==0]

arr=Zeroes+NonZeroes

print("After fifting Zeroes to the Rifght:",arr)
