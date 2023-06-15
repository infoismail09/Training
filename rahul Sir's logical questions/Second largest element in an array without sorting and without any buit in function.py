#  WAP to find Second largest element in an array : arr[] = [12, 35, 1, 10, 34, 1, 35], without 
# sorting, without using any built-in methods and without deleting duplicate elements. What will be 
# the time complexity?


def calc_largest(arr):  
    second_largest = arr[0]  
    largest_val = arr[0]  
    for i in range(len(arr)):  
        if arr[i] > largest_val:  
            largest_val = arr[i]  
  
    for i in range(len(arr)):  
        if arr[i] > second_largest and arr[i] != largest_val:  
            second_largest = arr[i]  
  
    return second_largest  
print(calc_largest([12, 35, 1, 10, 34, 1, 35]))
