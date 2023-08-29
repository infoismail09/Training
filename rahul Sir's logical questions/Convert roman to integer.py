# Convert roman to integer

def romanToInt(s):
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    for char in s[::-1]:
        value = roman_dict[char]
        if value >= prev_value:
            total += value
        else:
            total -= value
        prev_value = value
    
    return total

s = "LVIII"
output = romanToInt(s)
print(output)

# Output: 58
