

# Initialize defaultdict for character counts
from collections import defaultdict

def find_longest_substring(s, k):
    counts = defaultdict(int)
    left = ans = 0
    
    # Sliding window: expand right pointer
    for right in range(len(s)):
        counts[s[right]] += 1
        # Shrink window if too many distinct characters
        while len(counts) > k:
            counts[s[left]] -= 1
            if counts[s[left]] == 0:
                del counts[s[left]]
            left += 1
        
        # Update max substring length
        ans = max(ans, right - left + 1)
    
    return ans

string = "eceba"
print(find_longest_substring(string, 2))  
# Output: 3


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––






# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––














# how to identidy time and space
# how to know if  aquestion is commonly asked


# What is point of this from typing import List


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
