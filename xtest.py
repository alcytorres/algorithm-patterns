
def runningSum(nums):
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(prefix[-1] + nums[i])

    return prefix

nums = [1,2,3,4]
print(runningSum(nums))
# Output: [1,3,6,10]

# Time: O(n) - Iterates through n elements once to build the prefix sum array with O(1) operations per iteration.
# Space: O(n) - Uses a prefix sum array of size n to store the running sums, excluding input.




# prefix[j] - prefix[i - 1]
# prefix[j] - prefix[i] + nums[i]


# # Template 1
# def fn(arr):
#     prefix = [arr[0]]
#     for i in range(1, len(arr)):
#         prefix.append(prefix[-1] + arr[i])
    
#     return prefix

# print(fn([1, 6, 3, 2, 7, 2]))


# # Template 2
# def prefix_sum(arr):
#     prefix = [arr[0]]  # Array to store prefix sums, starts with first element
#     curr = arr[0]      # Tracks running sum for building prefix array
    
#     for i in range(1, len(arr)):  # Iterate from index 1
#         # Add current element to running sum
#         curr += arr[i]
#         # Append running sum to prefix array
#         prefix.append(curr)
    
#     return prefix  # Return prefix sum array for subarray sum queries

# print(prefix_sum([1, 6, 3, 2, 7, 2]))
