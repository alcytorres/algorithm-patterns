# Example 1: Longest Subarray with Sum Less Than or Equal to k

# Finds the length of the longest subarray with sum <= k using sliding window.

# Example 1: nums = [1, 2, 1, 2, 4, 2], k = 6
# Output: 4 (subarray [2, 1, 2, 1], sum = 6)

# Example 2: nums = [3, 1, 2, 7, 4, 2, 1, 1, 5], k = 8
# Output = 4 (subarray [4, 2, 1, 1], sum = 8)

def longest_subarray_sum(nums, k):
    l = curr = ans = 0

    for r in range(len(nums)):
        curr += nums[r]

        while curr >= k:
            curr -= nums[l]
            l += 1
        
        ans = max(ans, r - l + 1)
    
    return ans

nums = [1, 2, 3]
print(longest_subarray_sum(nums, 5))
# Output: 2
