# 977. Squares of a Sorted Array

# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
 
# Example 1:
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

# Example 2:
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

# Solution: https://leetcode.com/problems/squares-of-a-sorted-array/description/


def sortedSquares(nums):
    n = len(nums)
    result = [0] * n
    left = 0
    right = n - 1

    for i in range(n - 1, -1, -1):
        if abs(nums[left]) < abs(nums[right]):
            square = nums[right]
            right -= 1
        else:
            square = nums[left]
            left += 1
        
        result[i] = square * square
    
    return result


numbers = [-10, -5, 1, 2, 4, 7]
print(sortedSquares(numbers))  
# Output: [1, 4, 16, 25, 49, 100]


# Time: O(n) - Iterates through n elements once, with O(1) operations (comparisons, squaring, assignment) per iteration.
# Space: O(n) - Uses a result array of size n to store squared values, with only two integer pointers (left, right) as constant extra space.


# Space: O(n) if you take output into account and O(1) otherwise.




# Breakdown 
def sortedSquares(nums):
    n = len(nums)            # Get length of input array
    result = [0] * n         # Initialize result array of size n with zeros
    left = 0                 # Left pointer starts at beginning of array
    right = n - 1            # Right pointer starts at end of array
    
    for i in range(n - 1, -1, -1):    # Iterate backwards from n-1 to 0 to fill result
        if abs(nums[left]) < abs(nums[right]):  # Compare absolute values at pointers
            square = nums[right]          # Use right element if its absolute value is larger
            right -= 1                    # Move right pointer inward
        else:
            square = nums[left]           # Use left element if its absolute value is larger or equal
            left += 1                     # Move left pointer inward
        result[i] = square * square       # Square the chosen number and store in result
    return result                         # Return sorted array of squares

numbers = [-10, -5, 1, 2, 4, 7]
print(sortedSquares(numbers))  
# Output: [1, 4, 16, 25, 49, 100]


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Less efficeint solution

def sortedSquares(A):
    return sorted(x*x for x in A)  # Square each element and sort in one line

numbers = [-10, -5, 1, 2, 4, 7]
print(sortedSquares(numbers)) 
# Output: [1, 4, 16, 25, 49, 100]


# Time: O(n log n) - Generates n squared values in O(n) time, followed by sorting with Python's Timsort algorithm in O(n log n).
# Space: O(n) - Stores n squared values in the output list, with O(log n) auxiliary space used by Timsort for sorting operations.

# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Less efficeint solution

def sortedSquares(nums):
    ans = []
    for num in nums:
        ans.append(num * num)
    
    ans.sort()
    return ans

numbers = [-10, -5, 1, 2, 4, 7]
print(sortedSquares(numbers))  
# Output: [1, 4, 16, 25, 49, 100]


# Time: O(n log n) - Iterates through n elements to square in O(n) time, followed by sorting the result array in O(n log n) using Timsort.
# Space: O(n) - Uses a result array of size n to store squared values, with O(log n) auxiliary space for Timsort’s sorting process.

