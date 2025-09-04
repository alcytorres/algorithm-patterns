# Checking for existence

# Checking for Existence with Hash Maps/Sets
# Key Idea: Use hash maps (dictionaries) or sets to check if an element exists in O(1) time, improving algorithms from O(n²) to O(n).

# === Why Use Hashing for Existence? ===
# - Arrays/lists: Searching takes O(n), leading to O(n²) for nested checks.
# - Hash Maps/Sets: O(1) lookup, insertion, deletion (average case).
# - Reduces time complexity in problems needing fast existence checks.

# === Core Concepts ===
# - Hash Map: Stores key-value pairs (e.g., number -> index). Use when you need to track additional info (like indices).
# - Set: Stores unique elements only. Use when you just need to check existence (no duplicates or extra data).
# - Pre-processing: Convert input to a hash map/set first for O(1) lookups later.
# - Use Cases: Find pairs, duplicates, or missing elements quickly.

# === Python Examples ===
# 1. Hash Map for Existence with Extra Data (e.g., Two Sum)
#    - Problem: Find indices of two numbers in nums adding to target.
#    - Why Hash Map? Store number -> index for O(1) lookup of complement.

def twoSum(nums, target):
    d = {}
    for i in range(len(nums)):
        num = nums[i]
        complement = target - num

        if complement in d:  # O(1) check
            return [i, d[complement]]
        
        d[num] = i  # Store number and index

    return []

# 2. Set for Simple Existence (e.g., First Letter to Appear Twice)
#    - Problem: Find first character in string s that repeats.
#    - Why Set? Only need to check if seen before, no extra data.

def repeatedCharacter(s):
    seen = set()
    for c in s:
        if c in seen:  # O(1) check
            return c
        seen.add(c)  # Add to set
    
    return ""


# 3. Set for Multiple Conditions (e.g., Numbers with No Adjacent Values)
#    - Problem: Find numbers x where x+1 and x-1 are not in nums.
#    - Why Set? Pre-process nums into set for O(1) checks of x+1, x-1.

def find_numbers(nums):
    seen = set(nums)  # {2, 4, 6}
    ans = []
    
    for x in seen:
        if x+1 not in seen and x-1 not in seen:
            ans.append(x)
    return ans


# === When to Use ===
# - Hash Map: When you need to map elements to values (e.g., indices, counts).
# - Set: When you only care about existence or uniqueness.
# - If you see "if ... in ..." in a loop, consider hashing to make it O(1).

# === Time and Space Complexity ===
# - Time: O(n) for building hash map/set, O(1) for lookups.
# - Space: O(n) for storing up to n elements.
# - Tradeoff: Uses more memory than arrays but saves time.

# === Tips for LeetCode ===
# - Pre-process input into a hash map/set to avoid O(n) searches.
# - Use defaultdict for counting or when keys may be missing.
# - Sets are great for problems needing unique elements or no duplicates.
# - Always consider hashing when checking for pairs, duplicates, or gaps.