# 977. Squares of a Sorted Array

# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
 
# Example:
# Input: nums = [-4, -1, 0, 3, 10]
# Output:       [0, 1, 9, 16, 100]
# Explanation: After squaring, the array becomes [16, 1, 0, 9, 100].
# After sorting, it becomes [0, 1, 9, 16, 100].

# Solution: https://leetcode.com/problems/squares-of-a-sorted-array/description/

def sortedSquares(nums):
    n = len(nums)
    ans = [0] * n
    left = 0
    right = n - 1

    for i in range(n - 1, -1, -1):
        if abs(nums[left]) < abs(nums[right]):
            square = nums[right]
            right -= 1
        else:
            square = nums[left]
            left += 1
        
        ans[i] = square * square
    
    return ans


numbers = [-4, -1, 0, 3, 10]
print(sortedSquares(numbers))  
# Output: [0, 1, 9, 16, 100]


# Time: O(n) - Iterates through n elements once, with O(1) operations (comparisons, squaring, assignment) per iteration.
# Space: O(n) - Uses a ans array of size n to store squared values, with only two integer pointers (left, right) as constant extra space.

# Space: O(n) if you take output into account and O(1) otherwise.


# Trace Overview
# i      = 4    3  2  1  0
# right  = 4 3     2
# left   = 0    1     2  3
# square = 10  -4  3 -1  0
# ans    = [0, 0, 0, 0, 0] 
#          [0, 0, 0, 0, 100]
#          [0, 0, 0, 16, 100]
#          [0, 0, 9, 16, 100]
#          [0, 1, 9, 16, 100]
#          [0, 1, 9, 16, 100]


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown 
def sortedSquares(nums):
    n = len(nums)            # Get length of input array
    ans = [0] * n         # Initialize ans array of size n with zeros
    left = 0                 # Left pointer starts at beginning of array
    right = n - 1            # Right pointer starts at end of array
    
    for i in range(n - 1, -1, -1):    # Iterate backwards from n-1 to 0 to fill ans
        if abs(nums[left]) < abs(nums[right]):  # Compare absolute values at pointers
            square = nums[right]          # Use right element if its absolute value is larger
            right -= 1                    # Move right pointer inward
        else:
            square = nums[left]           # Use left element if its absolute value is larger or equal
            left += 1                     # Move left pointer inward
        ans[i] = square * square       # Square the chosen number and store in ans
    return ans                         # Return sorted array of squares




# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Task: Given a sorted array of integers, return a new array of squares in non-decreasing order.
# Example: nums = [-10, -5, 1, 2, 4, 7] → Output = [1, 4, 16, 25, 49, 100]
# Why: Practices two-pointer technique to efficiently sort squares without sorting the entire ans.

def sortedSquares(nums):  # Example: nums = [-10, -5, 1, 2, 4, 7]

    # 1️⃣ Initialize variables
    # Get the length of the input array
    # Why? We need the size to create the ans array and set pointer bounds
    n = len(nums)  # n = 6

    # Initialize ans array of size n with zeros
    # Why? We will fill this array with sorted squares
    ans = [0] * n  # ans = [0, 0, 0, 0, 0, 0]

    # Initialize left pointer at the start of the array
    # Why? We compare elements from both ends to find the largest absolute value
    left = 0  # left = 0

    # Initialize right pointer at the end of the array
    # Why? We start from the largest potential values (considering absolute values)
    right = n - 1  # right = 6 - 1 = 5

    # 2️⃣ Fill ans array backwards
    # Iterate from n-1 to 0 (backwards) to place largest squares first
    # Why? The largest square comes from the largest absolute value, so we fill from the end
    for i in range(n - 1, -1, -1):  # i goes from 5 to 0
        # --- Iteration 1: i = 5 ---
        # Compare absolute values at left and right pointers
        # Why? The larger absolute value produces the larger square
        if abs(nums[left]) < abs(nums[right]):  # abs(nums[0]) = |-10| = 10, abs(nums[5]) = |7| = 7
                                               # 10 < 7 is false, skip to else
            square = nums[right]  # skip
            right -= 1  # skip
        else:
            square = nums[left]  # square = nums[0] = -10
            left += 1  # left = 0 + 1 = 1
        # Square the chosen number and store in ans
        ans[i] = square * square  # ans[5] = (-10) * (-10) = 100
        # After Iteration 1: left = 1, right = 5, ans = [0, 0, 0, 0, 0, 100]

        # --- Iteration 2: i = 4 ---
        if i == 4:
            if abs(nums[left]) < abs(nums[right]):  # abs(nums[1]) = |-5| = 5, abs(nums[5]) = |7| = 7
                                                   # 5 < 7 is true
                square = nums[right]  # square = nums[5] = 7
                right -= 1  # right = 5 - 1 = 4
            else:
                square = nums[left]  # skip
                left += 1
            ans[i] = square * square  # ans[4] = 7 * 7 = 49
            # After Iteration 2: left = 1, right = 4, ans = [0, 0, 0, 0, 49, 100]

        # --- Iteration 3: i = 3 ---
        if i == 3:
            if abs(nums[left]) < abs(nums[right]):  # abs(nums[1]) = |-5| = 5, abs(nums[4]) = |4| = 4
                                                   # 5 < 4 is false
                square = nums[right]
                right -= 1
            else:
                square = nums[left]  # square = nums[1] = -5
                left += 1  # left = 1 + 1 = 2
            ans[i] = square * square  # ans[3] = (-5) * (-5) = 25
            # After Iteration 3: left = 2, right = 4, ans = [0, 0, 0, 25, 49, 100]

        # --- Iteration 4: i = 2 ---
        if i == 2:
            if abs(nums[left]) < abs(nums[right]):  # abs(nums[2]) = |1| = 1, abs(nums[4]) = |4| = 4
                                                   # 1 < 4 is true
                square = nums[right]  # square = nums[4] = 4
                right -= 1  # right = 4 - 1 = 3
            else:
                square = nums[left]
                left += 1
            ans[i] = square * square  # ans[2] = 4 * 4 = 16
            # After Iteration 4: left = 2, right = 3, ans = [0, 0, 16, 25, 49, 100]

        # --- Iteration 5: i = 1 ---
        if i == 1:
            if abs(nums[left]) < abs(nums[right]):  # abs(nums[2]) = |1| = 1, abs(nums[3]) = |2| = 2
                                                   # 1 < 2 is true
                square = nums[right]  # square = nums[3] = 2
                right -= 1  # right = 3 - 1 = 2
            else:
                square = nums[left]
                left += 1
            ans[i] = square * square  # ans[1] = 2 * 2 = 4
            # After Iteration 5: left = 2, right = 2, ans = [0, 4, 16, 25, 49, 100]

        # --- Iteration 6: i = 0 ---
        if i == 0:
            if abs(nums[left]) < abs(nums[right]):  # abs(nums[2]) = |1| = 1, abs(nums[2]) = |1| = 1
                                                   # 1 < 1 is false
                square = nums[right]
                right -= 1
            else:
                square = nums[left]  # square = nums[2] = 1
                left += 1  # left = 2 + 1 = 3
            ans[i] = square * square  # ans[0] = 1 * 1 = 1
            # After Iteration 6: left = 3, right = 2, ans = [1, 4, 16, 25, 49, 100]

    # 3️⃣ Return the sorted array of squares
    # Why? ans contains the squares of the input array in non-decreasing order
    return ans  # ans = [1, 4, 16, 25, 49, 100]


numbers = [-10, -5, 1, 2, 4, 7]
print(sortedSquares(numbers))  # Output: [1, 4, 16, 25, 49, 100]





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

# Time: O(n log n) - Iterates through n elements to square in O(n) time, followed by sorting the ans array in O(n log n) using Timsort.
# Space: O(n) - Uses a ans array of size n to store squared values, with O(log n) auxiliary space for Timsort’s sorting process.
