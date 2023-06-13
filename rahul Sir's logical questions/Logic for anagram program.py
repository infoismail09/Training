#  logic for anagram program with its time complexity. (for large strings)

a=input("Enter string 1:")
b=input("Enter string 2:")
count=0
for i in a:
    for j in b:
        if i==j:
            count=count+1
if count==len(a):
    print("Strings are anagram of each other.")
else:
    print("Strings are not anagram of each other.")
