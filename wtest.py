# Ask Claude, Grok, ChatGPT to name the top 50 most common DSA problems you rec I know.
# In the prompt find a way to include the ones you already have pracitced



# Organize mini guides doc. Delete the bottom part that says delete

# how do you know to do this ans = [0] * n   ?
# its not something intuitive. be realistic how you would think of that or if thats just comes down to memory?

# Review slicing arrays




#   a = (b × whole times) + leftover

# n % 10   # get the last digit
# n // 10  # remove the last digit



# What is point of this from typing import List

"""
Review common_algorithms.py 

Check on CLAUDE if the examples at the bottom of 09-0_Binary Search.py are worth knowing or if the 2 I practice are enough

Run operators.py guide through Claude to make it better? maybe more examples 
"""






# Find Pair with Target Sum in Sorted Array
"""
Given a sorted array of unique integers and a target integer, return true if there exists a pair of numbers that sum to target, false otherwise. 

This problem is similar to Two Sum. (In Two Sum, the input is not sorted).

Example
    Input: nums = [1, 3, 4, 6, 8, 10, 12], target = 14
    Output: True
    Explanation: nums[2] + nums[5] = 4 + 10 = 14 matches the target.
"""

# Solution: Two Pointers: Target Sum Pair Search

def find_pair_sum(nums, target):
    l = 0
    r = len(nums) - 1

    while l < r:
        if nums[l] + nums[r] < target:
            l += 1
        elif nums[l] + nums[r] > target:
            r -= 1
        else:
            return True
    
    return False


nums = [1, 3, 4, 6, 8, 10, 12]
target = 14
print(find_pair_sum(nums, target))  
# Output: True -> nums[2] + nums[5] = 4 + 10 = 14 matches the target.
