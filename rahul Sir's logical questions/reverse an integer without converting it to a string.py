# WAP to reverse an integer without converting it to a string, without using any builtin methods.

rev =0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
print("Reverse of the number:",rev)
    
