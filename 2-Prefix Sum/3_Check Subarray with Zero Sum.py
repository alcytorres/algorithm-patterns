# 3. Check Subarray with Zero Sum
"""
Task: Determine if an array has a subarray summing to zero. Return false otherwise.
Example: [1, 3, -4, 5] → True  (1 + 3 + -4 = 0)
Example: [1, 2, -2, 3] → True  (2 + -2 = 0)
Example: [4, -4, 1] → True  (4 + -4 = 0)
Why: Introduces prefix sum applications beyond simple running sums.
"""

def has_zero_sum_subarray(arr):

    # 1️⃣ Initialize prefix sum and set for tracking
    prefix_sum = 0
    seen = set()

    # 2️⃣ Iterate through the array to compute prefix sums
    for num in arr:
        prefix_sum += num  # Update running sum
        if prefix_sum == 0 or prefix_sum in seen:
            return True  
        seen.add(prefix_sum)

    # 3️⃣ Return False if no zero-sum subarray is found
    return False

# Test the function
print(has_zero_sum_subarray([1, 3, -4, 5,])) # Output: True  (1 + 3 + -4 = 0)
print(has_zero_sum_subarray([1, 3, 5, -4]))  # Output: False (no chunk sums to 0)
print(has_zero_sum_subarray([1, 2, -2, 3]))  # Output: True (2 + -2 = 0)

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

# Test the function


"""
Explnation: 
Imagine you are adding numbers in a list, step-by-step, and you are looking for a trick: if at any point your total either hits 0 or matches a total you have seen before, you’ve found a chunk of numbers that adds up to 0. That’s what this code does.

The code checks if there is a piece of the list [4, -4, 1] that adds to 0 (like 4 + -4 = 0). It keeps a running total and uses a “memory box” to remember totals it’s seen. If the total ever becomes 0 or repeats a number from the box, it says “Yes!” (True). If not, it says “No!” (False).

If we say True we exit the loop (and the whole function).
    - No more loop, no more numbers, just True because [4, -4] works.
    - It is like finding the answer and running out the door!
"""



# ----------------------------------------------------------------------------------
# Solution with Output Full Breakdown 

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
# Solution with output FUll Breakdown

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
# Solution with output

def has_zero_sum_subarray(arr):  # Example: arr = [3, -3, 1]

    # 1️⃣ Initialize prefix sum and set for tracking
    # Initialize prefix sum to 0
    prefix_sum = 0               # prefix_sum = 0
    
    # Create an empty set to store seen prefix sums
    seen = set()                 # seen = {}
    # After initialization: prefix_sum = 0, seen is empty

    # 2️⃣ Iterate through the array to compute prefix sums
    # Loop through each element in the array
    for num in arr:              # arr = [3, -3, 1]
        
        # --- Iteration 1: num = 3 ---
        # Update prefix sum by adding the current element
        prefix_sum += num        # prefix_sum = 0 + 3 = 3
        
        # Check if prefix sum is 0 or already in seen set
        if prefix_sum == 0 or prefix_sum in seen:  # prefix_sum = 3, 3 == 0 → False
                                                  # seen = {}, 3 in seen → False
            return True                           # Skip (no zero-sum subarray yet)
        
        # Add current prefix sum to seen set
        seen.add(prefix_sum)     # seen = {3}
        # After Iteration 1: prefix_sum = 3, seen = {3}
        # Current state: No zero-sum subarray found

        # --- Iteration 2: num = -3 ---
        prefix_sum += num        # prefix_sum = 3 + (-3) = 0
        if prefix_sum == 0 or prefix_sum in seen:  # prefix_sum = 0, 0 == 0 → True
                                                  # (No need to check seen since 0 == 0 is True)
            return True                           # Return True (subarray [3, -3] sums to 0)
        seen.add(prefix_sum)     # Skip (function returns before this)
        # After Iteration 2: Function returns True
        # Current state: Found subarray [3, -3] with sum 3 + (-3) = 0
        # Loop terminates early due to return

        # --- Iteration 3: num = 1 ---
        # Note: Not executed due to early return in Iteration 2

    # 3️⃣ Return False if no zero-sum subarray is found
    return False             # Skip (not reached due to early return)
    # Final state: Returned True in Iteration 2
    # Conclusion: Successfully identified a subarray [3, -3] with sum 0

print(has_zero_sum_subarray([3, -3, 1]))  # Output: True (3 + -3 = 0)



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
