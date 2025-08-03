# Example 3: Given an integer array nums, find all the numbers x in nums that satisfy the following: x + 1 is not in nums, and x - 1 is not in nums.

# If a valid number x appears multiple times, you only need to include it in the answer once.

# Example:
# Input: nums = [2, 4, 6, 8]
# Output: [2, 4, 6, 8]
# Explanation: For each x in nums, neither x+1 nor x-1 exists in nums (e.g., for x=2, 3 and 1 are absent; for x=4, 5 and 3 are absent). All numbers satisfy the condition, and duplicates are not an issue here.

def find_numbers(nums):
    seen = set(nums)  # {8, 2, 4, 6}
    ans = []
    for x in set(nums):
        if x+1 not in seen and x-1 not in seen:
            ans.append(x)
    return ans

l = [2, 4, 6, 8]
print(find_numbers(l))


# Time: O(n), where n is the length of nums (set conversion and iteration).
# Space: O(n) for the seen set and ans list.