# 2248. Intersection of Multiple Arrays

# Example 2: 

# Given a 2D array nums that contains n arrays of distinct integers, return a sorted array containing all the numbers that appear in all n arrays.

# For example, given nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]], return [3, 4]. 3 and 4 are the only numbers that are in all arrays.

# Example:
# Input: nums = [[3,1,2,4,5], [1,2,3,4], [3,4,5,6]]
# Output: [3, 4]
# Explanation: 
# The only integers present in each of nums[0] = [3,1,2,4,5], nums[1] = [1,2,3,4], and nums[2] = [3,4,5,6] are 3 and 4, so we return [3,4].

# Solution: https://leetcode.com/problems/intersection-of-multiple-arrays/solutions/


from collections import defaultdict

def intersection(nums):
    counts = defaultdict(int)
    for arr in nums:
        for x in arr:
            counts[x] += 1

    n = len(nums)
    ans = []
    for key in counts:
        if counts[key] == n:
            ans.append(key)
    
    return sorted(ans)

nums = [[3,1,2,4,5], [1,2,3,4], [3,4,5,6]]
print(intersection(nums))
# Output: [3, 4]
