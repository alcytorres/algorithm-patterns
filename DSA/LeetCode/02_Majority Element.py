# 169. Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Example 1:
#     Input: nums = [3, 2, 3]
#     Output: 3

# Example 2:
#     Input: nums = [2, 2, 1, 1, 1, 2, 2]
#     Output: 2
 
# Constraints:
#     n == nums.length
#     1 <= n <= 5 * 104
#     -109 <= nums[i] <= 109
#     The input is generated such that a majority element will exist in the array.
 
# Follow-up: Could you solve the problem in linear time and in O(1) space?


# Optpion 1
def majorityElement(nums):
    count = {}
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    return max(count, key=count.get)

nums = [3, 2, 3]
print(majorityElement(nums))


"""
Time: O(N)
  - Let N = length of nums.
  - Single pass to count frequencies → O(N).
      • Each insertion/update in the hash map is O(1) average.
  - Finding the max-frequency key is O(U), where U ≤ N.
  - Overall: O(N).

Space: O(N)
  - Hash map 'count' stores frequency of each unique number.
  - In worst case (all numbers different), stores N keys.
  - Overall: O(N).

  
Interview Answer: Worst Case

Time: O(N)
  - Count each element once, then take the max.

Space: O(N)
  - Hash map stores counts for all unique numbers.
"""


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown 
def majorityElement(nums):
    count = {}    # Dictionary to store frequency of each number
    for num in nums:     # Go through every number in the array
        if num in count:     # If we've seen this number before
            count[num] += 1  # Increment its count
        else:                # If it's the first time seeing it
            count[num] = 1   # Start counting it with 1
    
    return max(count, key=count.get)  # Return the number with highest count



# Follow-up: Could you solve the problem in linear time and in O(1) space?

# Boyer–Moore Voting Algorithm Solution
def majorityElement(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1

    return candidate

nums = [3, 2, 3]
print(majorityElement(nums))





# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown – Boyer–Moore Voting Algorithm 
def majorityElement(nums):
    count = 0          # Voting counter – how many "votes" the current candidate has
    candidate = None   # Current candidate for majority element

    for num in nums:       # One pass through the array
        if count == 0:     # No active candidate (votes dropped to zero)
            candidate = num # Elect the current number as new candidate
        
        # Vote for or against the candidate
        count += 1 if num == candidate else -1  
        # Same → +1 vote
        # Different → -1 vote (cancels one vote for candidate)

    return candidate   # Guaranteed to be the majority element



# (O(n) time
# O(1) space)







# Option 2
from collections import defaultdict

def majorityElement(nums):
    counts = defaultdict(int)

    for num in nums:
        counts[num] += 1

    max_count = 0
    majorityNum = None

    for key, value in counts.items():
        if value > max_count:
            majorityNum = key
            max_count = value
    
    return majorityNum

nums = [3, 2, 3]
print(majorityElement(nums))



# Option 3
def majorityElement_Simple(nums):
    # 1. Initialize a dictionary to store element counts
    counts = {}

    # 2. Iterate through the array and count frequencies
    for num in nums:
        # If the number is already a key, increment its count.
        # Otherwise, add it with a starting count of 1.
        counts[num] = counts.get(num, 0) + 1

    # 3. Determine the majority threshold
    n = len(nums)
    majority_threshold = n // 2  # integer division gives floor(n/2)

    # 4. Find the element whose count exceeds the threshold
    for num, count in counts.items():
        if count > majority_threshold:
            return num

nums = [3, 2, 3]
print(majorityElement(nums))


# Option 4
from collections import Counter

def majorityElement(nums):
    counts = Counter(nums)
    return max(counts.keys(), key=counts.get)

nums = [3, 2, 3]
print(majorityElement(nums))


# Option 5
def majorityElement(nums):
    nums.sort()
    return nums[len(nums) // 2]

nums = [3, 2, 3]
print(majorityElement(nums))

# Time: O(nlgn)
# Space: O(1) or (O(n))


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Brute Force
def majorityElement(nums):
    majority_count = len(nums) // 2
    
    for num in nums:
        count = sum(1 for elem in nums if elem == num)
        if count > majority_count:
            return num




# DICTIONARY METHOD: 
.get()