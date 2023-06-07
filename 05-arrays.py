# Arrays (called lists in python)
arr = [1, 2, 3]
print(arr) # [1, 2, 3]

# Can be used as a stack
arr.append(4)
arr.append(5)
print(arr) # [1, 2, 3, 4, 5]

arr.pop() # This will remove the last element of the list
print(arr) # [1, 2, 3, 4]

arr.insert(1, 7) # This will insert 7 in the number 1 position
print(arr) # [1, 7, 2, 3, 4] 

# But this is not recommended way as the Big O is Big O(n)
# Instead we can use the indexes to assign value
# But this will replaces the the current properties
arr[0] = 0
arr[3] = 0
print(arr) # [0, 7, 2,0, 4]

# Initialize arr of size n with default value of 1
n = 5
arr2 = [1] * n
print(arr2) # [1, 1, 1, 1, 1]
print(len(arr2)) # 5

# We can get the value of specific indexes by specifying the index number
print(arr[1]) #7

# if we want to get the last value we can use the minus and it will count backwards
print(arr[-1]) #4

# Sublists (aka slicing)
arr3 = [1,2, 3, 4]
print(arr3[1: 3]) # [2, 3]


