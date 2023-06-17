#Find prime numbers from 1 ....n 

# Python Program to print n prime No using for loop
  
No = int(input(" Please Enter any No: "))
 
print("Prime Nos between", 1, "and", No, "are:")
 
for Nomber in range(1, No + 1):
   # all prime Nos are greater than 1
   if Nomber > 1:
       for i in range(2, Nomber):
           if (Nomber % i) == 0:
               break
       else:
           print(Nomber)
