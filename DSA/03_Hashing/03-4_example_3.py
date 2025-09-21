# Numbers Without Adjacent Values

# Example 3: 
    # Given an integer array nums, find all the numbers x in nums that satisfy the following: x + 1 is not in nums, and x - 1 is not in nums.

# If a valid number x appears multiple times, you only need to include it in the answer once.

# Example:
    # Input: nums = [2, 4, 4, 6]
    # Output:       [2, 4, 6]
    # Explanation: For each x in nums, neither x+1 nor x-1 exists in nums (e.g., for x=2, 3 and 1 are absent; for x=4, 5 and 3 are absent). All numbers satisfy the condition, and duplicates are not an issue here.

def find_numbers(nums):
    seen = set(nums)  # {2, 4, 6}
    ans = []
    
    for x in seen:
        if x+1 not in seen and x-1 not in seen:
            ans.append(x)
    return ans

l = [2, 4, 4, 6]
print(find_numbers(l))
# Output: [2, 4, 6]

# Time: O(n)
# - Creating the set from nums: O(n).
# - Looping through 'seen': O(n) in the worst case.
# - Set lookups ('x+1 not in seen', 'x-1 not in seen') are O(1) on average.
# - Overall: O(n) time.

# Space: O(n)
# - Set 'seen' stores up to n elements: O(n) space.
# - List 'ans' can store up to n elements in the worst case: O(n) space.
# - A few variables (x) take O(1) space.
# - Overall: O(n) total space.


"""
Overview for Each Iteration
Input: nums = [2, 4, 4, 6]
Step 1: Create set of unique numbers
seen = {2, 4, 6}

Step 2: Check each number for valid conditions (x+1 and x-1 not in seen)
x   | x+1 | x-1 | x+1 in seen | x-1 in seen | ans
----|-----|-----|-------------|-------------|----------
2   | 3   | 1   | False       | False       | [2]
4   | 5   | 3   | False       | False       | [2, 4]
6   | 7   | 5   | False       | False       | [2, 4, 6]
Final: [2, 4, 6]


Most IMPORTANT thing to Understand:
    • We want numbers where neither neighbor (x+1 or x-1) is present in the array.

    • Using a set removes duplicates and makes lookups using `in` fast O(1).

    • The result only includes each valid number once, even if it appears multiple times.

    
Why this code Works:
    • seen (a set) holds all unique numbers so we don't double-count.

    • For each number x, check if both x+1 and x-1 are missing. If so, add x.

    • Efficiency: O(n) because building the set and checking neighbors are constant-time on average.

    • Intuition: Think of it like neighbors on a street — we only keep the houses with no one living next door.

TLDR
    • Build a set of numbers, keep only those with no neighbors (x+1 or x-1) in the set.

    
Quick Example Walkthrough:
nums = [2, 4, 4, 6]

    Step 1: Make set → seen = {2, 4, 6}

    Step 2: Check each number:
        2: 1 and 3 not in set → keep 2.
        4: 3 and 5 not in set → keep 4.
        6: 5 and 7 not in set → keep 6.

Final Answer: [2, 4, 6]


---------------------------------------------------
Q: How is the requirement that each valid number x appears only once in the answer handled?
    • Converting nums to a set (seen = set(nums)), removes duplicates. 

    • The for loop then iterates over unique numbers in seen, ensuring each valid x is added to ans only once.


Q: Why do we use 'for x in seen' ?   
    • Lets us directly test each unique number against the condition (x+1 not in seen and x-1 not in seen).

    • Avoids wasted checks on duplicates.

    • Ensures only valid, unique numbers get added.

"""


# 🔑 Set vs List Lookup (Why in is Faster with Sets)

# Set Lookup → O(1)
    # 👉 Uses hashing, jumps straight to where 4 would be stored.
s = {2, 4, 6}
print(4 in s)   # True, found instantly (O(1))
print(5 in s)   # False, checked instantly (O(1))


# List Lookup → O(n)
    # 👉 Has to check each element one by one until done.
l = [2, 4, 6]
print(4 in l)   # True, but Python may scan up to index 1 (O(n))
print(5 in l)   # False, Python scans all elements (O(n))





# ––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown 
def find_numbers(nums):
    seen = set(nums)          # Convert array to set for O(1) lookups
    ans = []                  # Initialize empty result list
    for x in seen:            # Iterate over unique numbers in set
        if x+1 not in seen and x-1 not in seen:  # Check if x+1 and x-1 absent
            ans.append(x)     # Add x to result if condition met
    return ans                # Return list of numbers without adjacent values



# ––––––––––––––––––––––––––––––––––––––––––––––––
# Alternative Solution

def find_numbers(nums):
    nums_set = set(nums)
    ans = [num for num in nums_set if num + 1 not in nums_set and num - 1 not in nums_set]

    return ans

l = [2, 4, 4, 6]
print(find_numbers(l))  
# Output: [2, 4, 6]



# ––––––––––––––––––––––––––––––––––––––––––––––––
# Task: Find all numbers x in an array such that x+1 and x-1 are not in the array, including each valid x once.
# Example: nums = [2, 4, 4, 6] → Output = [2, 4, 6] (all numbers satisfy: no x+1 or x-1 in nums)
# Why: Practices hash set usage for efficient lookup of adjacent values.

def find_numbers(nums):  # Example: nums = [2, 4, 4, 6]

    # 1️⃣ Create a set from the input array
    # Convert nums to a set for O(1) lookup
    # Why? We need to quickly check if x+1 and x-1 exist, and a set ensures unique elements
    seen = set(nums)  # seen = {2, 4, 6}

    # 2️⃣ Initialize result array
    # Create an empty list to store valid numbers
    # Why? We need to collect numbers that satisfy the condition
    ans = []  # ans = []

    # 3️⃣ Iterate through unique numbers in the set
    # Check each unique number x in seen
    # Why? We only need to check each distinct number once, and check if x+1 and x-1 are absent
    for x in seen:  # x takes values [2, 4, 6] (order may vary due to set)
        # --- Iteration 1: x = 2 ---
        # Check if x+1 and x-1 are not in the set
        # Why? A number is valid if both its adjacent values are absent
        if x + 1 not in seen and x - 1 not in seen:  # x = 2, x+1 = 3, x-1 = 1
                                                    # 3 not in {2, 4, 6}, 1 not in {2, 4, 6}, True
            ans.append(x)  # ans = [2]
        # After Iteration 1: ans = [2]

        # --- Iteration 2: x = 4 ---
        if x == 4:
            if x + 1 not in seen and x - 1 not in seen:  # x = 4, x+1 = 5, x-1 = 3
                                                        # 5 not in {2, 4, 6}, 3 not in {2, 4, 6}, True
                ans.append(x)  # ans = [2, 4]
            # After Iteration 2: ans = [2, 4]

        # --- Iteration 3: x = 6 ---
        if x == 6:
            if x + 1 not in seen and x - 1 not in seen:  # x = 6, x+1 = 7, x-1 = 5
                                                        # 7 not in {2, 4, 6}, 5 not in {2, 4, 6}, True
                ans.append(x)  # ans = [2, 4, 6]
            # After Iteration 3: ans = [2, 4, 6]

    # 4️⃣ Return the result
    # Why? ans contains all unique numbers x where x+1 and x-1 are not in the array
    return ans  # ans = [2, 4, 6]


l = [2, 4, 4, 6]
print(find_numbers(l))  
# Output: [2, 4, 6]
