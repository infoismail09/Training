find frequency of each and every character in a string.

string = "Engineer"

for i in string:
    frequency = string.count(i)
    print(str(i) + ": " + str(frequency), end=", ")
