# Numbers Without Adjacent Values

# Example 3: Given an integer array nums, find all the numbers x in nums that satisfy the following: x + 1 is not in nums, and x - 1 is not in nums.

# If a valid number x appears multiple times, you only need to include it in the answer once.

# Example:
# Input: nums = [2, 4, 6, 8]
# Output:       [2, 4, 6, 8]
# Explanation: For each x in nums, neither x+1 nor x-1 exists in nums (e.g., for x=2, 3 and 1 are absent; for x=4, 5 and 3 are absent). All numbers satisfy the condition, and duplicates are not an issue here.

def find_numbers(nums):
    seen = set(nums)  # {8, 2, 4, 6}
    ans = []
    for x in seen:
        if x+1 not in seen and x-1 not in seen:
            ans.append(x)
    return ans

l = [2, 4, 6, 8]
print(find_numbers(l))
# Output: [8, 2, 4, 6]

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



# Why do we use 'for x in seen'
    # To iterate over unique numbers in nums, ensuring each valid x is processed and added to the result only once, as required by the problem (duplicates are ignored).


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
# Task: Find all numbers x in an array such that x+1 and x-1 are not in the array, including each valid x once.
# Example: nums = [2, 4, 6, 8] → Output = [2, 4, 6, 8] (all numbers satisfy: no x+1 or x-1 in nums)
# Why: Practices hash set usage for efficient lookup of adjacent values.

def find_numbers(nums):  # Example: nums = [2, 4, 6, 8]

    # 1️⃣ Create a set from the input array
    # Convert nums to a set for O(1) lookup
    # Why? We need to quickly check if x+1 and x-1 exist, and a set ensures unique elements
    seen = set(nums)  # seen = {2, 4, 6, 8}

    # 2️⃣ Initialize result array
    # Create an empty list to store valid numbers
    # Why? We need to collect numbers that satisfy the condition
    ans = []  # ans = []

    # 3️⃣ Iterate through unique numbers in the set
    # Check each unique number x in seen
    # Why? We only need to check each distinct number once, and check if x+1 and x-1 are absent
    for x in seen:  # x takes values [2, 4, 6, 8] (order may vary due to set)
        # --- Iteration 1: x = 2 ---
        # Check if x+1 and x-1 are not in the set
        # Why? A number is valid if both its adjacent values are absent
        if x + 1 not in seen and x - 1 not in seen:  # x = 2, x+1 = 3, x-1 = 1
                                                    # 3 not in {2, 4, 6, 8}, 1 not in {2, 4, 6, 8}, True
            ans.append(x)  # ans = [2]
        # After Iteration 1: ans = [2]

        # --- Iteration 2: x = 4 ---
        if x == 4:
            if x + 1 not in seen and x - 1 not in seen:  # x = 4, x+1 = 5, x-1 = 3
                                                        # 5 not in {2, 4, 6, 8}, 3 not in {2, 4, 6, 8}, True
                ans.append(x)  # ans = [2, 4]
            # After Iteration 2: ans = [2, 4]

        # --- Iteration 3: x = 6 ---
        if x == 6:
            if x + 1 not in seen and x - 1 not in seen:  # x = 6, x+1 = 7, x-1 = 5
                                                        # 7 not in {2, 4, 6, 8}, 5 not in {2, 4, 6, 8}, True
                ans.append(x)  # ans = [2, 4, 6]
            # After Iteration 3: ans = [2, 4, 6]

        # --- Iteration 4: x = 8 ---
        if x == 8:
            if x + 1 not in seen and x - 1 not in seen:  # x = 8, x+1 = 9, x-1 = 7
                                                        # 9 not in {2, 4, 6, 8}, 7 not in {2, 4, 6, 8}, True
                ans.append(x)  # ans = [2, 4, 6, 8]
            # After Iteration 4: ans = [2, 4, 6, 8]

    # 4️⃣ Return the result
    # Why? ans contains all unique numbers x where x+1 and x-1 are not in the array
    return ans  # ans = [2, 4, 6, 8]


l = [2, 4, 6, 8]
print(find_numbers(l))  # Output: [2, 4, 6, 8]