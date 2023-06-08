# printing nuber Sequence using while loop :-

n = int(input("Enter the number:"))

i = 1

while i <= n :
    j = 1
    while j <= n-i+1:
        print(j,end = "")
        j = j +1
        
    print()
    i = i+1
