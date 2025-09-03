# Prefix Sum Techniques in Python

# Generic Template for Prefix Sum problems.
def prefix_sum(arr):
    prefix = [arr[0]]  # Array to store prefix sums, starts with first element
    curr = arr[0]      # Tracks running sum for building prefix array

    for i in range(1, len(arr)):  # Iterate from index 1
        # Add current element to running sum
        curr += arr[i]
        # Append running sum to prefix array
        prefix.append(curr)
    
    return prefix  # Return prefix sum array for subarray sum queries

# Time: O(n) - Single pass to build prefix sum array.
# Space: O(n) - Stores prefix sum array of size n.

# ––––––––––––––––––––––––––––––––––––––––––––––––
# Example 1: Query Subarray Sums with Limit
# Returns boolean array indicating if subarray sums from x to y are less than limit.
def check_subarray_sums(nums, queries, limit):
    prefix = [0]     # Prefix sum array, starts with 0 for index -1
    curr = 0         # Tracks running sum
    
    for num in nums:  # Build prefix sum
        curr += num   # Add current element
        prefix.append(curr)
    
    ans = []         # Store results for each query
    for x, y in queries:  # Iterate over queries
        # Sum from x to y is prefix[y+1] - prefix[x]
        subarray_sum = prefix[y + 1] - prefix[x]
        ans.append(subarray_sum < limit)
    
    return ans

print(check_subarray_sums([1, 6, 3, 2, 7, 2], [[0, 3], [2, 5], [2, 4]], 13))  
# Output: [True, False, True]  --> Sums: [12, 14, 12], compared to limit 13.

# Time: O(n + m) - O(n) to build prefix, O(m) for m queries.
# Space: O(n) - Stores prefix sum array.

# ––––––––––––––––––––––––––––––––––––––––––––––––
# Example 2: Number of Ways to Split Array
# Counts ways to split array into two parts where first part sum >= second part sum.
def ways_to_split_array(nums):
    total = 0        # Total sum of array
    for num in nums: # Calculate total sum
        total += num
    
    left = 0         # Running sum of left section
    ans = 0          # Count of valid splits
    
    for i in range(len(nums) - 1):  # Iterate up to second-to-last index
        left += nums[i]            # Add current element to left sum
        right = total - left       # Right sum is total minus left sum
        if left >= right:          # If left sum >= right sum
            ans += 1               # Increment count
    
    return ans

print(ways_to_split_array([1, 2, 3, 4, 5]))  
# Output: 3  --> Splits at indices 0 (1>=12), 1 (3>=9), 2 (6>=5) are valid.

# Time: O(n) - Single pass to compute total and left sums.
# Space: O(1) - Uses only a few variables (total, left, ans).

# ––––––––––––––––––––––––––––––––––––––––––––––––
# Cheatsheet
# - Prefix Sum: Pre-compute array sums for O(1) subarray sum queries.
# - Build: Start with [0] or [arr[0]], add running sum for each element.
# - Query: Sum from i to j is prefix[j+1] - prefix[i] (adjust for i=0).
# - Space-Time Trade-off: O(n) space for O(n) build, O(1) queries vs. O(n^2) without.
# - Optimize Space: Use running sum variable instead of array when order is incremental.