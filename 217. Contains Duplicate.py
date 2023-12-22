# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

#  Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false


# ******** Bruteforce approach ***************** // T.C - O(n^2)

# def containsDuplicate(nums):

#     n = len(nums)
#     for i in range(n):
#         for j in range(i+1,n):

#             if nums[i]==nums[j]:
#                 return True
#     return False

# #driver code
# arr = [1,2,3,1]
# # arr = [1,2,3,4]
# result = containsDuplicate(arr)
# print(result)


# *************  Sorting (Time Complexity: O(n log n)) *************

# def containsDuplicate(nums):

#     nums.sort()
#     n = len(nums)

#     for i in range(1,n):
#         if nums[i] == nums[i-1]:
#             return True
#     return False

# #driver code
# arr = [1,2,3,1]
# # arr = [1,2,3,4]
# result = containsDuplicate(arr)
# print(result)
    
# ***************** HashSet (Time Complexity: O(n)) *********

def ContainsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
            seen.add(num)
    return False

#driver code
# arr = [1,2,3,1]
# arr = [1,2,3,4]
# result = ContainsDuplicate(arr)
# print(result)


# ***************** Dictionary (Time Complexity: O(n)) *********

def containsDuplicate(nums):
    num_dict = {}
    for num in nums:
        if num in num_dict:
            return True
        num_dict[num] = 1
    return False

#driver code
arr = [1,2,3,1]
# arr = [1,2,3,4]
result = containsDuplicate(arr)
print(result)
