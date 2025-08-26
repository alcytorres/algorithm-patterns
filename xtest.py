def numberOfSubarrays(self, nums: List[int], k: int) -> int:
    # keep a prefix count
    # we will track the number of odd numbers that appear up to and including a certain index
    # if odds - k appears at an earlier position in the array, then there must be k odds in between that index and this one
    #   - because the sum of odds - k + k = odds, the amount we currently have
    # so we will track the frequency that each number of odds appears
    #   - example: for [1, 2, 3], the prefix count would be [1, 1, 2]
    #   - frequency would be {1: 2, 2: 1}
    # we can now add the frequency of odds - k at each index, as that represents all the start points that form a nice subarray with the current index as an end point

    ans = odds = 0
    freq = defaultdict(int)
    freq[0] = 1  # base case so that if we reach k odds for the first time, we add 1 to ans
    for num in nums:
        odds += num % 2  # odd number % 2 = 1, even % 2 = 0
        ans += freq[odds - k]
        freq[odds] += 1

    return ans





# from collections import defaultdict

# counts = defaultdict(int, {'a': 1, 'b': 2})

# print(counts['a'])
# print(counts['c'])
















# Why ans += counts[curr - k]?

# curr is the sum from start to current index.
# If curr - k is in counts, it means a previous sum exists where curr - prev = k, forming a subarray with sum k.
# counts[curr - k] tells how many such subarrays end at the current index.





# Trace Overview



# # how to identidy time and space
# # how to know if  aquestion is commonly asked


# # What is point of this from typing import List


# # prefix[j] - prefix[i - 1]
# # prefix[j] - prefix[i] + nums[i]


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
