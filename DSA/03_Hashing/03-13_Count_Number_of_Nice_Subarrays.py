# 1248. Count Number of Nice Subarrays

# Example 5
# Given an array of positive integers nums and an integer k. Find the number of subarrays with exactly k odd numbers in them.

# A continuous subarray is called nice if there are k odd numbers on it.


# Example 1:
# Input: nums = [1, 1, 2, 1, 1], k = 3
# Output: 2
# Explanation: The only sub-arrays with 3 odd numbers are [1, 1, 2, 1] and [1, 2, 1, 1].

# Solution: https://leetcode.com/problems/count-number-of-nice-subarrays/solutions/5349373/count-number-of-nice-subarrays/


from collections import defaultdict

def numberOfSubarrays(nums, k):
    counts = defaultdict(int)
    counts[0] = 1
    ans = odd = 0
    
    for num in nums:
        odd += num % 2
        ans += counts[odd - k]
        counts[odd] += 1

    return ans

nums = [1, 1, 2, 1, 1]
print(numberOfSubarrays(nums, 3))
# Output: 2 (subarrays [1, 1, 2, 1] and [1, 2, 1, 1])

# counts = 
# {0:1} 
# {0:1, 1:1} 
# {0:1, 1:1, 2:1} 
# {0:1, 1:1, 2:2} 
# {0:1, 1:1, 2:2, 3:1} 
# {0:1, 1:1, 2:2, 3:1, 4:1}

# Overview for Each Iteration
# Index = -  0  1  2  3  4
# num   = -  1  1  2  1  1
# curr  = 0  1  2  2  3  4
# ans   = 0  0  0  0  1  2



# Time: O(n)
# - Loop through nums once: O(n) iterations.
# - Dictionary lookups ('counts[curr - k]') and updates ('counts[curr] += 1') are O(1) on average.
# - Each element is processed once, no nested loops.
# - Overall: O(n) time.

# Space: O(n)
# - Dictionary 'counts' can store up to n different prefix sums in the worst case: O(n) space.
# - A few variables (curr, ans, num) take O(1) space.
# - Overall: O(n) total space.


# Most IMPORTANT thing to Understand for this solution:
# If we’ve seen a previous count of curr - k, then the subarray between that position and the current position has curr - (curr - k) = k odd numbers.

# Root of Why It Works
    # Hashing tracks counts: The hash map stores how many times we’ve seen each count of odd numbers, letting us quickly find pairs of positions where the difference in odd counts is k.

    # Prefix sum idea: curr acts like a prefix sum of odd numbers. A subarray with k odd numbers is found when curr - (previous curr) = k, or previous curr = curr - k.

    # Efficiency: Instead of checking every possible subarray, we use the hash map to count valid subarrays in one pass through the array.

    # This approach is like keeping a running tally of odd numbers and using a hash map to “remember” where we’ve been, so we can spot valid subarrays instantly.



# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Brute force
def numberOfSubarrays_bruteforce(nums, k):
    n = len(nums)
    ans = 0

    for i in range(n):
        odd_count = 0
        for j in range(i, n):
            if nums[j] % 2 == 1:
                odd_count += 1
            if odd_count == k:
                ans += 1
            elif odd_count > k:
                break
    return ans

nums = [1, 1, 2, 1, 1]
print(numberOfSubarrays_bruteforce(nums, 3))
# Output: 2


# Time: O(n^2)
# - Outer loop picks a start index i: O(n).
# - Inner loop extends subarray to j: O(n).
# - Each step does O(1) work (increment odd_count, compare to k).
# - Breaks early when odd_count > k, but worst-case is still O(n^2).
# - Overall: O(n^2) time.

# Space: O(1)
# - Only a constant number of variables (i, j, ans, odd_count) are used.
# - No additional data structures.
# - Overall: O(1) space.



# Trace Overview 
# nums = [1, 1, 2, 1, 1], k = 3
# i = 0 → j = 0: odd_count=1; j=1: odd_count=2; j=2: odd_count=2; j=3: odd_count=3 → ans=1; j=4: odd_count=4 → stop
# i = 1 → j = 1: odd_count=1; j=2: odd_count=1; j=3: odd_count=2; j=4: odd_count=3 → ans=2
# i = 2 → j = 2: odd_count=0; j=3: odd_count=1; j=4: odd_count=2 → never reaches 3
# i = 3 → j = 3: odd_count=1; j=4: odd_count=2 → never reaches 3
# i = 4 → j = 4: odd_count=1 → never reaches 3
# Final ans = 2



# –––––––––––––––––––––––––––––––––––––––––––––––
# Simple Breakdown 
from collections import defaultdict

def numberOfSubarrays(nums, k):
    counts = defaultdict(int)  # Notebook to track counts of odd numbers
    counts[0] = 1             # Start with "0 odds seen" once
    odd = ans = 0             # odd: count of odd numbers, ans: number of subarrays

    for num in nums:          # Iterate over each number
        odd += num % 2        # Add 1 if num is odd, 0 if even
        ans += counts[odd - k] # Check if we can make a subarray with k odds
        counts[odd] += 1      # Update notebook with current odd count
    
    return ans          # Return total subarrays with k odd numbers




# –––––––––––––––––––––––––––––––––––––––––––––––
# Full Breakdown

# Task: Count the number of subarrays with exactly k odd numbers in a positive integer array.
# Example: nums = [1, 1, 2, 1, 1], k = 3 → Output = 2 (subarrays: [1, 1, 2, 1], [1, 2, 1, 1])
# Why: Practices prefix sum technique with a hash map to count subarrays with a specific number of odd numbers.

from collections import defaultdict

def numberOfSubarrays(nums, k):  # Example: nums = [1, 1, 2, 1, 1], k = 3

    # 1️⃣ Initialize variables
    # Initialize a defaultdict to store counts of prefix sums of odd numbers
    # Why? We track the frequency of prefix sums (count of odd numbers) to find subarrays with k odd numbers
    counts = defaultdict(int)  # counts = {}
    counts[0] = 1  # Initialize with 0 odd numbers having 1 occurrence
    # Why? A prefix sum of 0 (no odd numbers) allows subarrays starting from index 0

    # Initialize answer to count subarrays with exactly k odd numbers
    # Why? We need to accumulate the number of valid subarrays
    ans = 0  # ans = 0

    # Initialize current count of odd numbers
    # Why? We track the running count of odd numbers to compute differences
    odd = 0  # odd = 0

    # 2️⃣ Process array to find subarrays
    # Iterate through each number to count odd numbers
    # Why? We use the count of odd numbers as a prefix sum to find subarrays with k odd numbers
    for num in nums:  # num takes values [1, 1, 2, 1, 1]
        # --- Iteration 1: num = 1 ---
        # Increment odd if the number is odd (num % 2 == 1)
        # Why? We count odd numbers to track the prefix sum of odd counts
        odd += num % 2  # num = 1, 1 % 2 = 1, odd = 0 + 1 = 1
        # Add the number of subarrays ending at the current index with k odd numbers
        # Why? If odd - k exists in counts, it means there are subarrays with k odd numbers
        ans += counts[odd - k]  # odd - k = 1 - 3 = -2, counts[-2] = 0 (not in counts), ans = 0
        # Increment the count of the current odd number prefix sum
        # Why? We track how many times this odd count has occurred
        counts[odd] += 1  # counts[1] = 0 + 1 = 1
        # After Iteration 1: odd = 1, ans = 0, counts = {0: 1, 1: 1}

        # --- Iteration 2: num = 1 ---
        if num == 1 and odd == 1:
            odd += num % 2  # num = 1, 1 % 2 = 1, odd = 1 + 1 = 2
            ans += counts[odd - k]  # odd - k = 2 - 3 = -1, counts[-1] = 0, ans = 0
            counts[odd] += 1  # counts[2] = 0 + 1 = 1
            # After Iteration 2: odd = 2, ans = 0, counts = {0: 1, 1: 1, 2: 1}

        # --- Iteration 3: num = 2 ---
        if num == 2:
            odd += num % 2  # num = 2, 2 % 2 = 0, odd = 2 + 0 = 2
            ans += counts[odd - k]  # odd - k = 2 - 3 = -1, counts[-1] = 0, ans = 0
            counts[odd] += 1  # counts[2] = 1 + 1 = 2
            # After Iteration 3: odd = 2, ans = 0, counts = {0: 1, 1: 1, 2: 2}

        # --- Iteration 4: num = 1 ---
        if num == 1 and odd == 2:
            odd += num % 2  # num = 1, 1 % 2 = 1, odd = 2 + 1 = 3
            ans += counts[odd - k]  # odd - k = 3 - 3 = 0, counts[0] = 1, ans = 0 + 1 = 1
            counts[odd] += 1  # counts[3] = 0 + 1 = 1
            # After Iteration 4: odd = 3, ans = 1, counts = {0: 1, 1: 1, 2: 2, 3: 1}
            # Found subarray: [1, 1, 2, 1] (3 odd numbers, indices 0 to 3)

        # --- Iteration 5: num = 1 ---
        if num == 1 and odd == 3:
            odd += num % 2  # num = 1, 1 % 2 = 1, odd = 3 + 1 = 4
            ans += counts[odd - k]  # odd - k = 4 - 3 = 1, counts[1] = 1, ans = 1 + 1 = 2
            counts[odd] += 1  # counts[4] = 0 + 1 = 1
            # After Iteration 5: odd = 4, ans = 2, counts = {0: 1, 1: 1, 2: 2, 3: 1, 4: 1}
            # Found subarray: [1, 2, 1, 1] (3 odd numbers, indices 1 to 4)

    # 3️⃣ Return the count of valid subarrays
    # Why? ans contains the number of subarrays with exactly k odd numbers
    return ans  # ans = 2


nums = [1, 1, 2, 1, 1]
print(numberOfSubarrays(nums, 3))  
# Output: 2 (subarrays [1, 1, 2, 1] and [1, 2, 1, 1])

# counts = 
# {0:1} -> {0:1, 1:1} -> {0:1, 1:2} -> {0:1, 1:2, 2:1} -> {0:1, 1:3, 2:1} -> {0:1, 1:4, 2:1}




# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Deep dive into why this solution works
from collections import defaultdict

def numberOfSubarrays(nums, k):
    counts = defaultdict(int)
    counts[0] = 1
    ans = odd = 0
    
    for num in nums:
        odd += num % 2
        ans += counts[odd - k]
        counts[odd] += 1

    return ans

nums = [1, 1, 2, 1, 1]
print(numberOfSubarrays(nums, 3))
# Output: 2 (subarrays [1, 1, 2, 1] and [1, 2, 1, 1])

# counts = 
# {0:1} 
# {0:1, 1:1} 
# {0:1, 1:1, 2:1} 
# {0:1, 1:1, 2:2} 
# {0:1, 1:1, 2:2, 3:1} 
# {0:1, 1:1, 2:2, 3:1, 4:1}


"""
What happens at index = 3, num = 1

At Index 3, num = 1 in nums = [1, 1, 2, 1] with k = 3:

What happens:
    • num % 2 = 1 (1 is odd), so curr (count of odd numbers) becomes 2 + 1 = 3.
    • Check curr - k = 3 - 3 = 0. The hash map has counts[0] = 1, so ans += 1 (becomes 1).
    • Update counts[3] += 1.

Why ans becomes 1:
    • curr = 3 means we’ve seen 3 odd numbers up to index 3: [1, 1, 2, 1].
    • curr - k = 0 means we’re looking for a previous point where we had 0 odd numbers.
    • counts[0] = 1 because before the array started (empty subarray), we had 0 odd numbers.
    • This tells us the subarray from the start (index -1, 0 odds) to index 3 (3 odds) has 3 - 0 = 3 odd numbers, which is exactly k. That’s the subarray [1, 1, 2, 1].

Simple idea:
    • The code finds a valid subarray because curr (3 odd numbers now) minus k (3) equals a previous count (0) in the hash map. This means the subarray between those points has exactly 3 odd numbers. The hash map tracks these counts to spot valid subarrays instantly.
"""

"""
What happens at index = 4, num = 1

Index 4, num = 1 in nums = [1, 1, 2, 1, 1] with k = 3:

What happens:
    • num % 2 = 1 (odd), so curr = 3 + 1 = 4.
    • Check curr - k = 4 - 3 = 1. counts[1] = 1, so ans += 1 (becomes 2).
    • Update counts[4] += 1.


Why ans becomes 2:
    • curr = 4 means 4 odd numbers up to index 4: [1, 1, 2, 1, 1].
    • curr - k = 1 means we need a previous point with 1 odd number.
    • counts[1] = 1 because at index 0, we had 1 odd number ([1]).
    • The subarray from index 1 to 4 ([1, 2, 1, 1]) has 4 - 1 = 3 odd numbers, matching k.

Simple idea:
    • The code finds the subarray [1, 2, 1, 1] because curr - k = 1 matches a previous count in the hash map, indicating a subarray with exactly 3 odd numbers.
"""
