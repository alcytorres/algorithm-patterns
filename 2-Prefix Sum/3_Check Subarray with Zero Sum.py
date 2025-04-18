# 3. Check Subarray with Zero Sum
"""
Task: Determine if an array has a subarray summing to zero. Return false otherwise.
Example: [4, -4, 1] → True  (4 + -4 = 0)
Why: Introduces prefix sum applications beyond simple running sums.
"""

def has_zero_sum_subarray(arr):
    prefix_sum = 0
    seen = set()
    for num in arr:
        prefix_sum += num  # Update running sum
        if prefix_sum == 0 or prefix_sum in seen:
            return True  # Zero sum found
        seen.add(prefix_sum)
    return False

# Test the function
print(has_zero_sum_subarray([4, -4, 1]))  # Output: True (4 + -4 = 0)
print(has_zero_sum_subarray([1, 2, -4]))  # Output: False (no chunk sums to 0)
print(has_zero_sum_subarray([1, 2, -3]))  # Output: True (1 + 2 + -3 = 0)

# Test the function
# Add this: print(seen) to see seen after each addition below this line: seen.add(prefix_sum)


# Solution
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

# Test the function
print(has_zero_sum_subarray([4, -4, 1]))  # Output: True (4 + -4 = 0)

"""
Explnation: 
Imagine you are adding numbers in a list, step-by-step, and you are looking for a trick: if at any point your total either hits 0 or matches a total you have seen before, you’ve found a chunk of numbers that adds up to 0. That’s what this code does.

The code checks if there is a piece of the list [4, -4, 1] that adds to 0 (like 4 + -4 = 0). It keeps a running total and uses a “memory box” to remember totals it’s seen. If the total ever becomes 0 or repeats a number from the box, it says “Yes!” (True). If not, it says “No!” (False).

If we say True we exit the loop (and the whole function).
    - No more loop, no more numbers, just True because [4, -4] works.
    - It is like finding the answer and running out the door!
"""

# ----------------------------------------------------------------------------------
# Solution with output

def has_zero_sum_subarray(arr):        # arr = [4, -4, 1]
    prefix_sum = 0                     # prefix_sum = 0 (start with no total)
    seen = set()                       # seen = {} (empty set to store running totals)
    for num in arr:                    # Loop through arr: num = 4, -4, 1
                                       # Iteration 1: num = 4
        prefix_sum += num              # prefix_sum = 0 + 4 = 4
        if prefix_sum == 0 or prefix_sum in seen:  # 4 == 0? False, 4 in {}? False
            return True                # skip
        seen.add(prefix_sum)           # Add 4 to seen: seen = {4}
                                       # Iteration 2: num = -4
        prefix_sum += num              # prefix_sum = 4 + (-4) = 0
        if prefix_sum == 0 or prefix_sum in seen:  # 0 == 0? True
            return True                # Return True (found zero sum [4, -4]) → Exit the loop (and the whole function)
        seen.add(prefix_sum)           # skip (not reached)
    
    return False                       # skip (not reached)


print(has_zero_sum_subarray([4, -4, 1]))  # Output: True (4 + -4 = 0)

# Test the function
# Add this: print(seen) to see seen after each addition below this line: seen.add(prefix_sum)
# seen = {4} 


# ----------------------------------------------------------------------------------
# Solution with output: [1, 2, -4]

def has_zero_sum_subarray(arr):        # arr = [1, 2, -4]
    prefix_sum = 0                     # prefix_sum = 0 (start with no total)
    seen = set()                       # seen = {} (empty set to store running totals)
    for num in arr:                    # Loop through arr: num = 1, 2, -4
                                       # Iteration 1: num = 1
        prefix_sum += num              # prefix_sum = 0 + 1 = 1
        if prefix_sum == 0 or prefix_sum in seen:  # 1 == 0? False, 1 in {}? False
            return True                # skip
        seen.add(prefix_sum)           # Add 1 to seen: seen = {1}
                                       # Iteration 2: num = 2
        prefix_sum += num              # prefix_sum = 1 + 2 = 3
        if prefix_sum == 0 or prefix_sum in seen:  # 3 == 0? False, 3 in {1}? False
            return True                # skip
        seen.add(prefix_sum)           # Add 3 to seen: seen = {1, 3}
                                       # Iteration 3: num = -4
        prefix_sum += num              # prefix_sum = 3 + (-4) = -1
        if prefix_sum == 0 or prefix_sum in seen:  # -1 == 0? False, -1 in {1, 3}? False
            return True                # skip
        seen.add(prefix_sum)           # Add -1 to seen: seen = {1, 3, -1}
    return False                       # Return False (no zero sum found)


print(has_zero_sum_subarray([1, 2, -4]))  # Output: False (no chunk sums to 0)

# Test the function
# Add this: print(seen) to see seen after each addition below this line: seen.add(prefix_sum)
# seen = {1, 3, -1}


# ----------------------------------------------------------------------------------
# Solution with output: [1, 2, -3]

def has_zero_sum_subarray(arr):        # arr = [1, 2, -3]
    prefix_sum = 0                     # prefix_sum = 0 (start with no total)
    seen = set()                       # seen = {} (empty set to store running totals)
    for num in arr:                    # Loop through arr: num = 1, 2, -3
                                       # Iteration 1: num = 1
        prefix_sum += num              # prefix_sum = 0 + 1 = 1
        if prefix_sum == 0 or prefix_sum in seen:  # 1 == 0? False, 1 in {}? False
            return True                # skip
        seen.add(prefix_sum)           # Add 1 to seen: seen = {1}
                                       # Iteration 2: num = 2
        prefix_sum += num              # prefix_sum = 1 + 2 = 3
        if prefix_sum == 0 or prefix_sum in seen:  # 3 == 0? False, 3 in {1}? False
            return True                # skip
        seen.add(prefix_sum)           # Add 3 to seen: seen = {1, 3}
                                       # Iteration 3: num = -3
        prefix_sum += num              # prefix_sum = 3 + (-3) = 0
        if prefix_sum == 0 or prefix_sum in seen:  # 0 == 0? True
            return True                # Return True (found zero sum [1, 2, -3]) → Exit the loop (and the whole function)
        seen.add(prefix_sum)           # skip (not reached)

    return False                       # skip (not reached)


print(has_zero_sum_subarray([1, 2, -3]))  # Output: True (1 + 2 + -3 = 0)

# Test the function
# Add this: print(seen) to see seen after each addition below this line: seen.add(prefix_sum)
# seen = {1, 3}
