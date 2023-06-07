# Unpacking an array
a, b, c = [1, 2, 3]
print(a, b, c) # 1 2 3

# Be careful though, this throws an error as the length and the number od variables are not same
#x, y = [1, 2, 3]
#print(x, y) #ValueError: too many values to unpack 

# Looping through arrays
nums  = [1, 2, 3]

# using index
for i in range(len(nums)):
    print(nums[i]) # 1 2 3

# without index
for n in nums:
    print(n) # 1 2 3

# with index and value
for i, n in enumerate(nums):
    print(i, "  ", n) # 0 1
    # 0 2
    #0 3

# loop through multiple arrays simultaneously with unpacking
nums1 = [1, 3, 5]
nums2 = [2, 4, 6]
for n1, n2 in zip(nums1, nums2):
    print(n1, n2)
# 1 2
# 3 4
# 5 6

# Reverse
nums = [1, 2, 3]
nums.reverse()
print(nums) #[3, 2, 1]

# Sorting
arr = [5, 4, 7, 3, 8]
arr.sort()
print(arr) # [3, 4, 5, 7, 8]

arr.sort(reverse=True)
print(arr) # [8, 7, 5, 4, 3]

arr = ["bob", "alice", "jane", "doe"]
arr.sort()
print(arr) #['alice', 'bob', 'doe', 'jane']

# Custom sort (by length of string)
arr.sort(key=lambda x: len(x))
print(arr) # ['bob', 'doe', 'jane', 'alice']

# List comprehension
arr = [i for i in range(5)]
print(arr) # [0, 1, 2, 3, 4]

# 2-D Lists
arr = [[0] * 4 for i in range(4)]
print(arr) # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
print(arr[0][0], arr[3][3])

