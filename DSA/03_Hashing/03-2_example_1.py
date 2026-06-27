# 1. Two Sum
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example:
    Input: nums = [3, 1, 7, 4, -6], target = 5
    Output: [1, 3]
    Explanation: Because nums[1] + nums[3] == 5, we return [1, 3] or [3, 1].

Solution: https://leetcode.com/problems/two-sum/description/

Why: Practices efficient hash map usage for finding pairs with a specific sum.
"""

# ––––––––––––––––––––––––––––––––––––––––––––––––
# Enumerate-Based One-Pass Hash Map Solution

def twoSum(nums, target):
    d = {}

    for i, num in enumerate(nums):
        diff = target - num

        if diff in d:   # O(1) check
            return [i, d[diff]]
        d[num] = i      # Store number and index

    return []

nums = [3, 1, 7, 4, -6]
target = 5
print(twoSum(nums, target))  
# Output: [3, 1] → Indices [3, 1] correspond to numbers [4, 1], and 4 + 1 = 5 matches the target.

# Key   = number we have already seen
# Value = index where that number appears


# ––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown 
def twoSum(nums, target):
    d = {}    # Initialize dictionary for number-to-index mapping
    
    for i, num in enumerate(nums):  # Iterate with index and number
        diff = target - num         # Calculate complement needed for target

        if diff in d:            # If complement exists in dictionary
            return [i, d[diff]]  # Return current and complement's indices
        d[num] = i            # Store current number and its index

    return []                 # Return empty list if no solution found


"""
Time: O(N)
  - Let N = length of nums.
  - Loop through nums once → O(N).
      • For each num, check if (target - num) exists in dictionary → O(1) average.
      • Insert current num into dictionary → O(1).
  - Each element is processed exactly once.
  - Overall: O(N).

Space: O(N)
  - Dictionary 'd' stores up to N key-value pairs (num → index).
  - A few variables (i, num, diff) use O(1) space.
  - Overall: O(N).

  
Interview Answer: Worst Case

Time: O(N)
  - Single pass with constant-time hash lookups.

Space: O(N)
  - Dictionary stores previously seen numbers.


---
Overview for Each Iteration
Input: nums = [3, 1, 7, 4, -6], target = 5

Step: Find indices of two numbers summing to target
i | num | diff (target - num) | d               | Action
--|-----|---------------------|-----------------|--------------------------
0 | 3   | 2 (5 - 3)           | {3:0}           | Store 3 at index 0
1 | 1   | 4 (5 - 1)           | {3:0, 1:1}      | Store 1 at index 1
2 | 7   | -2 (5 - 7)          | {3:0, 1:1, 7:2} | Store 7 at index 2
3 | 4   | 1 (5 - 4)           | {3:0, 1:1, 7:2} | Found 1 in d, return [3, 1]

Final: [3, 1] (nums[1] + nums[3] = 1 + 4 = 5)


---
Most IMPORTANT thing to Understand:
    • As you scan the array, you want to know: “Have I already seen the number needed to complete the pair?”

    • For each current number num, the needed partner is diff = target - num.

    • A hash map lets you check instantly (O(1)) whether that partner has already appeared.

---
Why this code Works:
    • Hash map role:
        • d stores: number → index where it appeared.
        • This lets us check “Have we seen diff before?” in O(1).

    • Technique:
        • One-pass scan.
        • For each num, compute diff.
        • If diff is in the map → we found the pair.
        • Otherwise, store num in the map and continue.

    • Efficiency:
        • No nested loops.
        • Replace O(N²) brute force with O(N) by using constant-time lookups.

    • Intuition:
        • Like walking through a room with a checklist:
          “I need diff. Have I seen it already?” If yes, answer found.

---
TLDR:
    • Store numbers as you go and check if the complement (target - num) is already in the map — if so, return the two indices.

---
Quick Example Walkthrough:

    nums = [3, 1, 7, 4, -6], target = 5

    Map initially: {}

    i=0, num=3  
        diff = 5 - 3 = 2  
        2 not in map → store 3: d = {3:0}

    i=1, num=1  
        diff = 5 - 1 = 4  
        4 not in map → store 1: d = {3:0, 1:1}

    i=2, num=7  
        diff = 5 - 7 = -2  
        -2 not in map → store 7: d = {3:0, 1:1, 7:2}

    i=3, num=4  
        diff = 5 - 4 = 1  
        1 *is* in map → index = 1  
        Return [3, 1]

    Final Answer: [3, 1]


---
Q: Why do we use `d[num] = i` instead of `d[diff] = i`?

  • d is a lookup table of numbers we've already seen.

  • We store the current number (num) because it's the thing we HAVE.

  • We check for diff because it's the thing we NEED.

  • If diff is already in d → we found the pair.
  • If not → we save num so future numbers can match with it.

👉 d[num] = i means: "This number exists at this index."
👉 d[diff] = i would store a number we haven't seen yet, which makes no sense.


---
Q: Why do we include `return []` at the end?

  • The loop returns as soon as it finds a valid pair.
    
  • If no pair is found during the loop, the function must still return something.
    
  • Returning [] is just a safe fallback so the function always returns a valid value.

"""




# ––––––––––––––––––––––––––––––––––––––––––––––––
# Index-First Dictionary Approach

def twoSum(nums, target):
    d = {}

    for i in range(len(nums)):
        num = nums[i]
        diff = target - num

        if diff in d:
            return [i, d[diff]]
        
        d[num] = i

    return []

nums = [3, 1, 7, 4, -6]
target = 5
print(twoSum(nums, target))
# Output: [3, 1] or [1, 3] -> 1 + 4 = 5

"""
Time: O(n)
  - Loop through nums once: O(n) iterations.
  - Dictionary lookups ('if complement in d') and inserts ('d[num] = i') are O(1) on average.
  - No nested loops, so total time is O(n).

Space: O(n)
  - Dictionary 'd' can store up to n elements in the worst case (when no match is found until the end), O(n) space.
  - A few integer variables (i, num, complement) take O(1) space.
  - Overall: O(n) total space.
  - If we exclude the dictionary from consideration (not typical here since it's part of the algorithm), extra space is O(1).



Overview for Each Iteration
Input: nums = [3, 1, 7, 4, -6], target = 5

Step: Find indices of two numbers summing to target
i   | num  | diff (target - num) | d                 | Action
----|------|---------------------|-------------------|----------------
0   | 3    | 2 (5 - 3)          | {3: 0}             | Store 3 at index 0
1   | 1    | 4 (5 - 1)          | {3: 0, 1: 1}       | Store 1 at index 1
2   | 7    | -2 (5 - 7)         | {3: 0, 1: 1, 7: 2} | Store 7 at index 2
3   | 4    | 1 (5 - 4)          | {3: 0, 1: 1, 7: 2} | Found 1 in d, return [3, 1]

Final: [3, 1] (nums[1] + nums[3] = 1 + 4 = 5)

As soon as a difference matches a num you found the answer. In this case that difference is 1. 

"""

# ––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown 
def twoSum(nums, target):
    d = {}                     # Initialize empty dictionary for number-to-index mapping
    for i in range(len(nums)): # Iterate over array indices
        num = nums[i]          # Current number
        diff = target - num  # Calculate difference needed for target

        if diff in d:    # If difference exists in dictionary
            return [i, d[diff]]  # Return current index and difference's index
        
        d[num] = i             # Store current number and its index in dictionary
        
    return []                  # Return empty list if no solution found




# Pseudocode
# FUNCTION two_sum(nums, target)
#     // Step 1: Create an empty hash map to store number-to-index pairs
#     INITIALIZE hash_map as empty dictionary

#     // Step 2: Loop through the array with index and number
#     FOR EACH index, number IN ENUMERATE(nums)
#         // Step 3: Calculate the complement needed to reach target
#         SET complement = target - number

#         // Step 4: Check if complement exists in hash map
#         IF complement EXISTS IN hash_map
#             // Found a pair: return indices of complement and current number
#             RETURN [hash_map[complement], index]

#         // Step 5: Store current number and its index in hash map
#         SET hash_map[number] = index


# ––––––––––––––––––––––––––––––––––––––––––––––––
# Brute force Solution
def two_sum(nums, target):
    n = len(nums)   
    for i in range(n):
        for j in range(n):
            if i != j:
                curr_sum = nums[i] + nums[j]
                if curr_sum == target:
                    return [i, j]
    
    # Time: O(n^2)
    # Space: O(1)





