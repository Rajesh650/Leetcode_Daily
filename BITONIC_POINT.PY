"""
Given an array arr of n elements that is first strictly increasing and then maybe strictly decreasing, find the maximum element in the array.
Note: If the array is increasing then just print the last element will be the maximum value.

Example 1:

Input: 
n = 9
arr[] = {1,15,25,45,42,21,17,12,11}
Output: 45
Explanation: Maximum element is 45.
Example 2:

Input: 
n = 5
arr[] = {1, 45, 47, 50, 5}
Output: 50
Explanation: Maximum element is 50.

"""

# shortcut 
# def findMaximum(arr, n):

#     for i in arr:

#         max_element = max(arr)

#         return max_element

# #Driver code

# arr = {1, 45, 47, 50, 5}
# x = len(arr)
# result = findMaximum(arr,x)
# print(result)