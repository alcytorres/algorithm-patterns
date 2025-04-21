# 5. Partition Array into Equal Sums
"""
Task: Check if an array can be split into two non-empty contiguous parts with equal sums.
      i.e. Split an array into two next-to-each-other parts, where each part has at least one number and both parts add up to the same total.
Example 1: [1, 2, 3] → True (1 + 2 = 3)
Example 2: [1, 5, 6] → True (1 + 5 = 6)
Why: Reinforces cumulative sum usage.
"""

def can_partition(arr):
    total_sum = sum(arr)
    if total_sum % 2 != 0:
        return False  # Odd sum can't be split evenly
    target = total_sum // 2
    prefix_sum = 0
    for num in arr:
        prefix_sum += num
        if prefix_sum == target:
            return True  # Found a split point
    return False

print(can_partition([1, 2, 3]))  # Output: True (1 + 2 = 3)
print(can_partition([1, 5, 6]))  # Output: True (1 + 5 = 6)


# Solution
def can_partition(arr):    # Define the function that takes an array 'arr' as input
    """
    Checks if the array can be split into two parts with equal sums.
    
    - Uses prefix sum to find a point where left sum equals remaining sum.
    - Time Complexity: O(n), Space Complexity: O(1).
    - Iterative check is straightforward and beginner-friendly.
    """
    total_sum = sum(arr)     # Calculate the total sum of the array
    if total_sum % 2 != 0:   # If total sum is odd
        return False         # Cannot split into two equal integer sums
    target = total_sum // 2  # Each part should sum to half of total_sum
    prefix_sum = 0      # Initialize prefix sum to zero
    for num in arr:     # Iterate through each element in 'arr'
        prefix_sum += num  # Add the current number to the prefix sum
        if prefix_sum == target:  # If prefix sum equals the target
            return True   # A split point is found
    return False          # No split point found

# Test the function
# print(can_partition([1, 2, 3]))  # Output: True (1 + 2 = 3)


"""
Concise Walkthrough of Why can_partition Works

The can_partition function checks if an array can be split into two side-by-side parts, each with at least one number, that add up to the same total. Here is why it works, explained simply:

    1. Get Total Sum: It adds all numbers in the array (total_sum = sum(arr)). For [1, 2, 3], total_sum = 6.
    2. Check if Splittable: If total_sum is odd (e.g., 7), it can’t be split into two equal parts, so return False. For 6, it’s even, so continue.
    3. Find Target: Each part must sum to half the total (target = total_sum // 2). For 6, target = 3.
    4. Track Running Sum: It uses prefix_sum to add numbers one by one, checking if the sum so far hits the target. For [1, 2, 3]:
        - Add 1: prefix_sum = 1 (not 3, keep going).
        - Add 2: prefix_sum = 1 + 2 = 3 (equals 3, found a split: [1, 2] sums to 3, rest [3] sums to 3).
        - If prefix_sum equals target, return True.
    5. No Split Found: If no prefix_sum equals target after checking all numbers, return False.

Why It Works: By checking the running sum (prefix_sum) against half the total sum, it finds if there’s a point where the left part sums to target. Since the total sum is 2 * target, the remaining part (total_sum - prefix_sum) also equals target, ensuring both parts have equal sums. For [1, 2, 3], it finds [1, 2] (sum = 3) and [3] (sum = 3), so it returns True. The method is simple and checks each possible split point efficiently.
"""

"""
Why use this: target = total_sum // 2 instead of this: target = total_sum / 2
    - Target = total_sum // 2 sets the sum each split part needs (half the total). 
    - if total_sum % 2 != 0 confirms the total is even. 
    - Using / instead of // gives a float (e.g., 6 / 2 = 3.0), which may not match prefix_sum (an integer) in comparisons. // keeps target an integer (e.g., 3) for correct checks.
"""

# ----------------------------------------------------------------------------------
# Solution with output

def can_partition(arr):                 # arr = [1, 2, 3]
    total_sum = sum(arr)               # sum([1, 2, 3]) = 1 + 2 + 3 = 6
    if total_sum % 2 != 0:             # Is 6 % 2 != 0? No, 6 is even
        return False                   # skip
    target = total_sum // 2            # target = 6 // 2 = 3 (need part summing to 3)
    prefix_sum = 0                     # prefix_sum = 0 (start with no total)
    for num in arr:                    # Loop through arr: num = 1, 2, 3
                                       # Iteration 1: num = 1
        prefix_sum += num              # prefix_sum = 0 + 1 = 1
        if prefix_sum == target:       # Is 1 == 3? No
            return True                # skip
                                       # Iteration 2: num = 2
        prefix_sum += num              # prefix_sum = 1 + 2 = 3
        if prefix_sum == target:       # Is 3 == 3? Yes
            return True                # Return True (split found: [1, 2] sums to 3, [3] sums to 3)
                                       # Iteration 3: num = 3
        prefix_sum += num              # skip (not reached)
        if prefix_sum == target:       # skip (not reached)
            return True                # skip (not reached)
        
    return False                       # skip (not reached)

print(can_partition([1, 2, 3]))       # Output: True (1 + 2 = 3)


