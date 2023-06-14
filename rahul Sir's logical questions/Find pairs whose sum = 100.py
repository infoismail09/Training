def find(array, len, summ):
    print("Pairs whose sum is : ", summ)
    for i in range(len):
        for j in range(i, len):
            if (array[i] + array[j]) == summ:
                print(array[i], array[j])


array = [80, 60, 10, 50, 30, 100, 0, 50]

# Take sum as input from user
summ = 100

# print array
print("Array = ", array)

# call function find
find(array, len(array), summ)
