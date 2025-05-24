# 3. Check Subarray with Zero Sum
"""
Task: Determine if an array has a subarray summing to zero. Return false otherwise.

Example 1: [1, 3, -4, 5]  → True  (1 + 3 + -4 = 0)       → prefix_sums: [1, 4, 0, 5]
Example 2: [1, 2, -2, 3]  → True  (2 + -2 = 0)           → prefix_sums: [1, 3, 1, 4]
Example 3: [1, 2, -1, -1] → True  (1 + 2 = -1 -1)        → prefix_sums: [1, 3, 2, 1]

Example 4: [1, 3, 5, -4]  → False (no chunk sums to 0)   → prefix_sums: [1, 4, 9, 5]
Example 5: [4, -4, 1]     → True  (4 + -4 = 0)           → prefix_sums: [4, 0, 1]


Why: Uses prefix sums to detect subarrays with a sum of zero efficiently.
     Introduces prefix sum applications beyond simple running sums.
"""

def has_zero_sum_subarray(arr):

    # 1️⃣ Initialize prefix sum and set for tracking
    prefix_sum = 0
    seen = set()

    # 2️⃣ Iterate through the array to compute prefix sums
    for num in arr:
        prefix_sum += num   # Update running sum
        if prefix_sum == 0 or prefix_sum in seen:
            return True  
        seen.add(prefix_sum)

    # 3️⃣ Return False if no zero-sum subarray is found
    return False


print(has_zero_sum_subarray([1, 3, -4, 5,])) # Output: True  (1 + 3 + -4 = 0)
print(has_zero_sum_subarray([1, 3, 5, -4]))  # Output: False (no chunk sums to 0)
print(has_zero_sum_subarray([1, 2, -2, 3]))  # Output: True (2 + -2 = 0)
print(has_zero_sum_subarray([1, 2, -1, -1]))  # Output: True (2 + -1 -1 = 0)

print(has_zero_sum_subarray([3, -3, 1]))  # Output: True (3 + -3 = 0)
print(has_zero_sum_subarray([1, 2, -4]))  # Output: False (no chunk sums to 0)
print(has_zero_sum_subarray([1, 2, -3]))  # Output: True (1 + 2 + -3 = 0)

# Test the function
# Add this: print(seen) to see seen after each addition below this line: seen.add(prefix_sum)


# Simple Breakdown
def has_zero_sum_subarray(arr):    # Define the function that takes an array 'arr' as input
    """
    Determines if there exists a subarray with sum zero.
    
    - Tracks prefix sums in a set; a repeat or zero indicates a zero-sum subarray.
    - Time Complexity: O(n), Space Complexity: O(n) for the set.
    - Set-based approach is intuitive for beginners and efficient.
    """
    prefix_sum = 0      # Initialize prefix sum to zero
    seen = set()        # Create an empty set to store seen prefix sums

    for num in arr:     # Iterate through each element in 'arr'
        prefix_sum += num  # Add the current number to the prefix sum
        if prefix_sum == 0 or prefix_sum in seen:  # If prefix sum is zero or seen before
            return True   # A subarray with sum zero exists
        seen.add(prefix_sum)  # Add the current prefix sum to the set

    return False        # No subarray with sum zero found


print(has_zero_sum_subarray([1, 3, -4, 5,])) # Output: True  (1 + 3 + -4 = 0)


"""
Solution Explnation: 

Imagine you are adding numbers in a list, step-by-step, and you are looking for a trick: if at any point your total either hits 0 or matches a total you have seen before, you’ve found a chunk of numbers that adds up to 0. That’s what this code does.

The code checks if there is a piece of the list [4, -4, 1] that adds to 0 (like 4 + -4 = 0). It keeps a running total and uses a “memory box” to remember totals it’s seen. If the total ever becomes 0 or repeats a number from the box, it says “Yes!” (True). If not, it says “No!” (False).

If we say True we exit the loop (and the whole function).
    - No more loop, no more numbers, just True because [4, -4] works.
    - It is like finding the answer and running out the door!


# ----------------------------------------------------------------------------------
Key Lesson: Understanding `if prefix_sum == 0 or prefix_sum in seen:` and Its Top Use Cases

Purpose: Detects subarrays with a sum of 0 using prefix sums.

How it Works:
   - prefix_sum == 0: True if the subarray from the start to the current index sums to 0.
   - Example: arr = [2, -2] → prefix_sum = 2 + (-2) = 0 → True (subarray [2, -2]).

    - prefix_sum in seen: True if the current prefix sum matches a previous one, meaning the subarray between them sums to 0.
     Example: arr = [1, 2, -2] → prefix sums = [1, 3, 1]. Second prefix_sum = 1 matches first prefix_sum = 1, so 1 - 1 = 0 for subarray [2, -2] → True.

Top 2 Use Cases for Each:
    1. prefix_sum == 0:
    - Case 1: Subarray from start sums to 0.
      Example: arr = [3, -3] → prefix_sum = 3 + (-3) = 0 → True (subarray [3, -3]).

    - Case 2: Single zero element.
      Example: arr = [0] → prefix_sum = 0 → True (subarray [0]).

2. prefix_sum in seen:
    - Case 1: Subarray between indices sums to 0.
     Example: arr = [1, 2, -2] → prefix sums = [1, 3, 1]. Second prefix_sum = 1 matches first prefix_sum = 1, so 1 - 1 = 0 for subarray [2, -2] → True.

    - Case 2: Repeated prefix sum after multiple elements.
      Example: arr = [1, 2, 3, -6] → prefix sums = [1, 3, 6, 0]. When prefix_sum = 6 is seen, later prefix_sum = 6 (after 1+2+3+(-6)) appears again, so 6 - 6 = 0 for subarray [2, 3, -6] → True.

# Takeaway: `prefix_sum == 0` catches zero sums from the start or single zeros; `prefix_sum in seen` finds zero-sum subarrays between indices.


# ----------------------------------------------------------------------------------
Key Lesson: Which Condition Hits in `if prefix_sum == 0 or prefix_sum in seen:`

Purpose: Identifies which condition (`prefix_sum == 0` or `prefix_sum in seen`) triggers True in has_zero_sum_subarray.

Test Cases and Condition Hits:
1. [1, 3, -4, 5] → True: prefix_sum == 0
   - At index 2: prefix_sum = 1 + 3 + (-4) = 0 → True.
2. [1, 3, 5, -4] → False: Neither
   - No prefix_sum = 0, no repeated prefix sums in seen.
3. [1, 2, -2, 3] → True: prefix_sum in seen
   - Prefix sums = [1, 3, 1, 4]. At index 2: prefix_sum = 1, already in seen → True.
4. [1, 2, -1, -1] → True: prefix_sum in seen
   - Prefix sums = [1, 3, 2, 1]. At index 3: prefix_sum = 1, already in seen (from index 0) → True (subarray [2, -1, -1] sums to 0).

5. [4, -4, 1] → True: prefix_sum == 0
   - At index 1: prefix_sum = 4 + (-4) = 0 → True.
6. [1, 2, -4] → False: Neither
   - No prefix_sum = 0, no repeated prefix sums in seen. 
7. [1, 2, -3] → True: prefix_sum == 0
   - At index 2: prefix_sum = 1 + 2 + (-3) = 0 → True.

Takeaway: prefix_sum == 0 hits when the sum from start is 0; prefix_sum in seen hits when a subarray between indices sums to 0.
"""

# ----------------------------------------------------------------------------------
# Solution with Output Full Breakdown  → [1, 3, -4, 5]

def has_zero_sum_subarray(arr):  # Example: arr = [1, 3, -4, 5]

    # 1️⃣ Initialize prefix sum and set for tracking
    # Initialize prefix sum to 0
    # Why? We'll accumulate the sum of elements to compute prefix sums
    prefix_sum = 0               # prefix_sum = 0
    
    # Create an empty set to store seen prefix sums
    # Why? We track prefix sums to detect if a subarray sums to zero
    seen = set()                 # seen = {}
    # After initialization: prefix_sum = 0, seen is empty

    # 2️⃣ Iterate through the array to compute prefix sums
    # Loop through each element in the array
    # Why? We check if the current prefix sum is 0 or has been seen before
    for num in arr:              # arr = [1, 3, -4, 5]
        
        # --- Iteration 1: num = 1 ---
        # Update prefix sum by adding the current element
        # Why? Prefix sum at each step is the sum of elements up to that point
        prefix_sum += num        # prefix_sum = 0 + 1 = 1
        
        # Check if prefix sum is 0 or already in seen set
        # Why? A prefix sum of 0 or a repeated prefix sum indicates a subarray with sum 0
        if prefix_sum == 0 or prefix_sum in seen:  # prefix_sum = 1, 1 == 0 → False
                                                  # seen = {}, 1 in seen → False
            return True                           # Skip (no zero-sum subarray yet)
        
        # Add current prefix sum to seen set
        # Why? We store this prefix sum to detect future repeats
        seen.add(prefix_sum)     # seen = {1}
        # After Iteration 1: prefix_sum = 1, seen = {1}
        # Current state: No zero-sum subarray found

        # --- Iteration 2: num = 3 ---
        prefix_sum += num        # prefix_sum = 1 + 3 = 4
        if prefix_sum == 0 or prefix_sum in seen:  # prefix_sum = 4, 4 == 0 → False
                                                  # seen = {1}, 4 in seen → False
            return True                           # Skip
        seen.add(prefix_sum)     # seen = {1, 4}
        # After Iteration 2: prefix_sum = 4, seen = {1, 4}
        # Current state: No zero-sum subarray found

        # --- Iteration 3: num = -4 ---
        prefix_sum += num        # prefix_sum = 4 + (-4) = 0
        if prefix_sum == 0 or prefix_sum in seen:  # prefix_sum = 0, 0 == 0 → True
                                                  # (No need to check seen since 0 == 0 is True)
            return True                           # Return True (subarray [1, 3, -4] sums to 0)
        seen.add(prefix_sum)     # Skip (function returns before this)
        # After Iteration 3: Function returns True
        # Current state: Found subarray [1, 3, -4] with sum 1 + 3 + (-4) = 0
        # Loop terminates early due to return

        # --- Iteration 4: num = 5 ---
        # Note: Not executed due to early return in Iteration 3

    # 3️⃣ Return False if no zero-sum subarray is found
    # Why? If we complete the loop without finding a zero-sum subarray, none exists
    return False             # Skip (not reached due to early return)
    # Final state: Returned True in Iteration 3
    # Conclusion: Successfully identified a subarray [1, 3, -4] with sum 0

print(has_zero_sum_subarray([1, 3, -4, 5]))  # Output: True (1 + 3 + -4 = 0)



# ----------------------------------------------------------------------------------
# Solution with output FUll Breakdown  → [1, 2, -2, 3]

def has_zero_sum_subarray(arr):  # Example: arr = [1, 2, -2, 3]

    # 1️⃣ Initialize prefix sum and set for tracking
    # Initialize prefix sum to 0
    # Why? We'll accumulate the sum of elements to compute prefix sums
    prefix_sum = 0               # prefix_sum = 0
    
    # Create an empty set to store seen prefix sums
    # Why? We track prefix sums to detect if a subarray sums to zero
    seen = set()                 # seen = {}
    # After initialization: prefix_sum = 0, seen is empty

    # 2️⃣ Iterate through the array to compute prefix sums
    # Loop through each element in the array
    # Why? We check if the current prefix sum is 0 or has been seen before
    for num in arr:              # arr = [1, 2, -2, 3]
        
        # --- Iteration 1: num = 1 ---
        # Update prefix sum by adding the current element
        # Why? Prefix sum at each step is the sum of elements up to that point
        prefix_sum += num        # prefix_sum = 0 + 1 = 1
        
        # Check if prefix sum is 0 or already in seen set
        # Why? A prefix sum of 0 or a repeated prefix sum indicates a subarray with sum 0
        if prefix_sum == 0 or prefix_sum in seen:  # prefix_sum = 1, 1 == 0 → False
                                                  # seen = {}, 1 in seen → False
            return True                           # Skip (no zero-sum subarray yet)
        
        # Add current prefix sum to seen set
        # Why? We store this prefix sum to detect future repeats
        seen.add(prefix_sum)     # seen = {1}
        # After Iteration 1: prefix_sum = 1, seen = {1}
        # Current state: No zero-sum subarray found

        # --- Iteration 2: num = 2 ---
        prefix_sum += num        # prefix_sum = 1 + 2 = 3
        if prefix_sum == 0 or prefix_sum in seen:  # prefix_sum = 3, 3 == 0 → False
                                                  # seen = {1}, 3 in seen → False
            return True                           # Skip
        seen.add(prefix_sum)     # seen = {1, 3}
        # After Iteration 2: prefix_sum = 3, seen = {1, 3}
        # Current state: No zero-sum subarray found

        # --- Iteration 3: num = -2 ---
        prefix_sum += num        # prefix_sum = 3 + (-2) = 1
        if prefix_sum == 0 or prefix_sum in seen:  # prefix_sum = 1, 1 == 0 → False
                                                  # seen = {1, 3}, 1 in seen → True
            return True                           # Return True (subarray [2, -2] sums to 0)
        seen.add(prefix_sum)     # Skip (function returns before this)
        # After Iteration 3: Function returns True
        # Current state: Found subarray [2, -2] with sum 2 + (-2) = 0
        # Loop terminates early due to return

        # --- Iteration 4: num = 3 ---
        # Note: Not executed due to early return in Iteration 3

    # 3️⃣ Return False if no zero-sum subarray is found
    # Why? If we complete the loop without finding a zero-sum subarray, none exists
    return False             # Skip (not reached due to early return)
    # Final state: Returned True in Iteration 3
    # Conclusion: Successfully identified a subarray [2, -2] with sum 0

print(has_zero_sum_subarray([1, 2, -2, 3]))  # Output: True (2 + -2 = 0)



# ----------------------------------------------------------------------------------
# Solution with output FUll Breakdown  → [1, 2, -1, -1]

def has_zero_sum_subarray(arr):  # Example: arr = [1, 2, -1, -1]

    # 1️⃣ Initialize prefix sum and set for tracking
    # Initialize prefix sum to 0
    # Why? We'll accumulate the sum of elements to compute prefix sums
    prefix_sum = 0               # prefix_sum = 0
    
    # Create an empty set to store seen prefix sums
    # Why? We track prefix sums to detect if a subarray sums to zero
    seen = set()                 # seen = {}
    # After initialization: prefix_sum = 0, seen is empty

    # 2️⃣ Iterate through the array to compute prefix sums
    # Loop through each element in the array
    # Why? We check if the current prefix sum is 0 or has been seen before
    for num in arr:              # arr = [1, 2, -1, -1]
        
        # --- Iteration 1: num = 1 ---
        # Update prefix sum by adding the current element
        # Why? Prefix sum at each step is the sum of elements up to that point
        prefix_sum += num        # prefix_sum = 0 + 1 = 1
        
        # Check if prefix sum is 0 or already in seen set
        # Why? A prefix sum of 0 or a repeated prefix sum indicates a subarray with sum 0
        if prefix_sum == 0 or prefix_sum in seen:  # prefix_sum = 1, 1 == 0 → False
                                                  # seen = {}, 1 in seen → False
            return True                           # Skip (no zero-sum subarray yet)
        
        # Add current prefix sum to seen set
        # Why? We store this prefix sum to detect future repeats
        seen.add(prefix_sum)     # seen = {1}
        # After Iteration 1: prefix_sum = 1, seen = {1}
        # Current state: No zero-sum subarray found

        # --- Iteration 2: num = 2 ---
        prefix_sum += num        # prefix_sum = 1 + 2 = 3
        if prefix_sum == 0 or prefix_sum in seen:  # prefix_sum = 3, 3 == 0 → False
                                                  # seen = {1}, 3 in seen → False
            return True                           # Skip
        seen.add(prefix_sum)     # seen = {1, 3}
        # After Iteration 2: prefix_sum = 3, seen = {1, 3}
        # Current state: No zero-sum subarray found

        # --- Iteration 3: num = -1 ---
        prefix_sum += num        # prefix_sum = 3 + (-1) = 2
        if prefix_sum == 0 or prefix_sum in seen:  # prefix_sum = 2, 2 == 0 → False
                                                  # seen = {1, 3}, 2 in seen → False
            return True                           # Skip
        seen.add(prefix_sum)     # seen = {1, 3, 2}
        # After Iteration 3: prefix_sum = 2, seen = {1, 3, 2}
        # Current state: No zero-sum subarray found

        # --- Iteration 4: num = -1 ---
        prefix_sum += num        # prefix_sum = 2 + (-1) = 1
        if prefix_sum == 0 or prefix_sum in seen:  # prefix_sum = 1, 1 == 0 → False
                                                  # seen = {1, 3, 2}, 1 in seen → True
            return True                           # Return True (subarray [2, -1, -1] sums to 0)
        seen.add(prefix_sum)     # Skip (function returns before this)
        # After Iteration 4: Function returns True
        # Current state: Found subarray [2, -1, -1] with sum 2 + (-1) + (-1) = 0
        # Loop terminates early due to return

    # 3️⃣ Return False if no zero-sum subarray is found
    # Why? If we complete the loop without finding a zero-sum subarray, none exists
    return False             # Skip (not reached due to early return)
    # Final state: Returned True in Iteration 4
    # Conclusion: Successfully identified a subarray [2, -1, -1] with sum 0

print(has_zero_sum_subarray([1, 2, -1, -1]))  # Output: True (2 + -1 + -1 = 0)



# ----------------------------------------------------------------------------------
# Solution with output
# Example: arr = [4, -4, 1] → True (4 + -4 = 0)

def has_zero_sum_subarray(arr):  # Example: arr = [4, -4, 1]

    # 1️⃣ Initialize prefix sum and set for tracking
    # Initialize prefix sum to 0
    prefix_sum = 0               # prefix_sum = 0
    
    # Create an empty set to store seen prefix sums
    seen = set()                 # seen = {}
    # After initialization: prefix_sum = 0, seen is empty

    # 2️⃣ Iterate through the array to compute prefix sums
    # Loop through each element in the array
    for num in arr:              # arr = [4, -4, 1]
        
        # --- Iteration 1: num = 4 ---
        # Update prefix sum by adding the current element
        prefix_sum += num        # prefix_sum = 0 + 4 = 4
        
        # Check if prefix sum is 0 or already in seen set
        if prefix_sum == 0 or prefix_sum in seen:  # prefix_sum = 4, 4 == 0 → False
                                                  # seen = {}, 4 in seen → False
            return True                           # Skip (no zero-sum subarray yet)
        
        # Add current prefix sum to seen set
        seen.add(prefix_sum)     # seen = {4}
        # After Iteration 1: prefix_sum = 4, seen = {4}
        # Current state: No zero-sum subarray found

        # --- Iteration 2: num = -4 ---
        prefix_sum += num        # prefix_sum = 4 + (-4) = 0
        if prefix_sum == 0 or prefix_sum in seen:  # prefix_sum = 0, 0 == 0 → True
                                                  # (No need to check seen since 0 == 0 is True)
            return True                           # Return True (subarray [4, -4] sums to 0)
        seen.add(prefix_sum)     # Skip (function returns before this)
        # After Iteration 2: Function returns True
        # Current state: Found subarray [4, -4] with sum 4 + (-4) = 0
        # Loop terminates early due to return

        # --- Iteration 3: num = 1 ---
        # Note: Not executed due to early return in Iteration 2

    # 3️⃣ Return False if no zero-sum subarray is found
    return False             # Skip (not reached due to early return)
    # Final state: Returned True in Iteration 2
    # Conclusion: Successfully identified a subarray [4, -4] with sum 0


print(has_zero_sum_subarray([4, -4, 1]))  # Output: True (4 + -4 = 0)


# ----------------------------------------------------------------------------------
# Solution with output: [1, 2, -3]
# Example: arr = [1, 2, -3] → True (1 + 2 + -3 = 0)

def has_zero_sum_subarray(arr):  # Example: arr = [1, 2, -3]

    # 1️⃣ Initialize prefix sum and set for tracking
    # Initialize prefix sum to 0
    # Why? We'll accumulate the sum of elements to compute prefix sums
    prefix_sum = 0               # prefix_sum = 0
    
    # Create an empty set to store seen prefix sums
    # Why? We track prefix sums to detect if a subarray sums to zero
    seen = set()                 # seen = {}
    # After initialization: prefix_sum = 0, seen is empty

    # 2️⃣ Iterate through the array to compute prefix sums
    # Loop through each element in the array
    # Why? We check if the current prefix sum is 0 or has been seen before
    for num in arr:              # arr = [1, 2, -3]
        
        # --- Iteration 1: num = 1 ---
        # Update prefix sum by adding the current element
        # Why? Prefix sum at each step is the sum of elements up to that point
        prefix_sum += num        # prefix_sum = 0 + 1 = 1
        
        # Check if prefix sum is 0 or already in seen set
        # Why? A prefix sum of 0 or a repeated prefix sum indicates a subarray with sum 0
        if prefix_sum == 0 or prefix_sum in seen:  # prefix_sum = 1, 1 == 0 → False
                                                  # seen = {}, 1 in seen → False
            return True                           # Skip (no zero-sum subarray yet)
        
        # Add current prefix sum to seen set
        # Why? We store this prefix sum to detect future repeats
        seen.add(prefix_sum)     # seen = {1}
        # After Iteration 1: prefix_sum = 1, seen = {1}
        # Current state: No zero-sum subarray found

        # --- Iteration 2: num = 2 ---
        prefix_sum += num        # prefix_sum = 1 + 2 = 3
        if prefix_sum == 0 or prefix_sum in seen:  # prefix_sum = 3, 3 == 0 → False
                                                  # seen = {1}, 3 in seen → False
            return True                           # Skip
        seen.add(prefix_sum)     # seen = {1, 3}
        # After Iteration 2: prefix_sum = 3, seen = {1, 3}
        # Current state: No zero-sum subarray found

        # --- Iteration 3: num = -3 ---
        prefix_sum += num        # prefix_sum = 3 + (-3) = 0
        if prefix_sum == 0 or prefix_sum in seen:  # prefix_sum = 0, 0 == 0 → True
                                                  # (No need to check seen since 0 == 0 is True)
            return True                           # Return True (subarray [1, 2, -3] sums to 0)
        seen.add(prefix_sum)     # Skip (function returns before this)
        # After Iteration 3: Function returns True
        # Current state: Found subarray [1, 2, -3] with sum 1 + 2 + (-3) = 0
        # Loop terminates early due to return

    # 3️⃣ Return False if no zero-sum subarray is found
    # Why? If we complete the loop without finding a zero-sum subarray, none exists
    return False             # Skip (not reached due to early return)
    # Final state: Returned True in Iteration 3
    # Conclusion: Successfully identified a subarray [1, 2, -3] with sum 0


print(has_zero_sum_subarray([1, 2, -3]))  # Output: True (1 + 2 + -3 = 0)