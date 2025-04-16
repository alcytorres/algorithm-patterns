# 3. Check Subarray with Zero Sum
"""
Task: Determine if an array has a subarray summing to zero.
Example: [4, -4, 1] → True
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
Imagine you’re adding numbers in a list, step-by-step, and you’re looking for a trick: if at any point your total either hits 0 or matches a total you’ve seen before, you’ve found a chunk of numbers that adds up to 0. That’s what this code does.

The code checks if there’s a piece of the list [4, -4, 1] that adds to 0 (like 4 + -4 = 0). It keeps a running total and uses a “memory box” to remember totals it’s seen. If the total ever becomes 0 or repeats a number from the box, it says “Yes!” (True). If not, it says “No!” (False).
"""

# ----------------------------------------------------------------------------------
# Solution with output

def has_zero_sum_subarray(arr):        # arr = [4, -4, 1]
    prefix_sum = 0                     # prefix_sum = 0
    seen = set()                       # seen = {}
    for num in arr:                    # Iteration 1: num = 4
        prefix_sum += num              # prefix_sum = 0 + 4 = 4
        if prefix_sum == 0 or prefix_sum in seen:  # 4 == 0? False, 4 in {}? False
            return True                # skip
        seen.add(prefix_sum)           # seen = {4}
                                       # Iteration 2: num = -4
                                       # prefix_sum = 4 + (-4) = 0
                                       # 0 == 0? True
                                       # return True (found zero sum)
    return False                       # not reached

print(has_zero_sum_subarray([4, -4, 1]))  # Output: True (4 + -4 = 0)

# Test the function
# Add this: print(seen) to see seen after each addition below this line: seen.add(prefix_sum)
# seen = {4} 

