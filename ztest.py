"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
"""


def move_zeros(arr):

    non_zero_pos = 0

    for read in range(len(arr)):
        if arr[read] != 0:
            arr[non_zero_pos], arr[read] = arr[read], arr[non_zero_pos]
            non_zero_pos += 1

    return arr

print(move_zeros([0, 1, 0, 3, 12]))  # Output: [1, 3, 12, 0, 0]

print(move_zeros([3, 5, 0, 0, 4]))  # Output: [3, 5, 4, 0, 0]