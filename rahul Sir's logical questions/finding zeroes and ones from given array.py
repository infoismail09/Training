# finding zeroes and ones from given array


a = [0,1,0,1,0,1,0]

zeroes=0

ones=0

for i in a:
    if i == 0:
        zeroes=zeroes+1
    else:
        ones=ones+1
print(zeroes)
print(ones)
