# 1426. Counting Elements
"""
Given an integer array arr, count how many elements x there are, such that x + 1 is also in arr. 

If there are duplicates in arr, count them separately.

Example:
    Input: arr = [1, 2, 2, 3]
    Output: 3
    Explanation: 1, 2, and 2 are counted cause 2 and 3 are in arr.

Solution: https://leetcode.com/problems/counting-elements/solutions/567376/counting-elements/
"""

# Optimized Solution: Search with HashSet
def countElements(arr):
    hash_set = set(arr)
    count = 0
    
    for x in arr:
        if x + 1 in hash_set:
            count += 1
    return count

arr = [1, 2, 2, 3]
print(countElements(arr))
# Output: 3


"""
Time: O(N)
  - Let N = length of arr.
  - Step 1: Build a set from arr → O(N).
      • Each insertion takes O(1) average.
  - Step 2: Loop through arr → O(N).
      • For each element x, check if x + 1 is in the set → O(1) average.
  - Overall: O(N + N) = O(N).

Space: O(N)
  - The set 'hash_set' stores up to N unique numbers.
  - A few scalar variables (count, x) use O(1).
  - Overall: O(N).

  
Interview Answer: Worst Case

Time: O(N)
  - Build hash set and scan all elements once.

Space: O(N)
  - Hash set holds all unique values from arr.


---
Overview for Each Iteration
Input: arr = [1, 2, 2, 3]

Step 1: Create set of unique elements
hash_set = {1, 2, 3}

Step 2: Count elements x where x + 1 is in hash_set
x   | x + 1 | x + 1 in hash_set | count
----|-------|-------------------|------
1   | 2     | True              | 1
2   | 3     | True              | 2
2   | 3     | True              | 3
3   | 4     | False             | 3

Final: 3


---
Q: Why use a set instead of a array for lookups?
    • Set lookups are O(1) on average (hash table).
    • Array lookups are O(n) since they scan sequentially.

    
Q: What is the key idea of the solution?
    • Store all numbers in a hash set.
    • For each number x in arr, check if x+1 exists in the set.
    • Count it if true.

    
Q: Why do duplicates count separately?
    • We iterate through arr directly, so duplicates are checked individually.

"""


# ––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown

def countElements(arr):
    hash_set = set(arr)       # Convert array to set for O(1) lookups
    count = 0                 # Initialize counter for elements with x+1

    for x in arr:             # Iterate over each element in array
        if x + 1 in hash_set: # Check if x+1 exists in set
            count += 1        # Increment counter if x+1 found
    return count              # Return total count of valid elements



# ––––––––––––––––––––––––––––––––––––––––––––––––
# Counting Elements – Naive List Lookup Approach
    # This is valid but inefficient

def countElements(arr):
    seen = set(arr)
    count = 0
    
    for x in arr:
        if x+1 in arr:
            count += 1
    return count


arr = [1, 2, 2, 3]
print(countElements(arr))
# Output: 3

"""
Time: O(n^2)
  - Outer loop iterates over all n elements.
  - Each 'x + 1 in arr' check is a list lookup, which takes O(n) in the worst case.
  - Overall: O(n * n) = O(n^2) time.

Space: O(n)
  - Set 'seen' stores up to n elements: O(n) space.
  - A few variables (x, count) take O(1) space.
  - Overall: O(n) total space.



⚠️ Why This Solution is Inefficient
    • Each x+1 in arr lookup is O(n) because arr is a list.

    • You do this for every element (n iterations).

    • Total time complexity = O(n²).

    • For small inputs, fine. For large arr (like 10⁵ elements), this will time out on LeetCode.

"""



# –––––––––––––––––––––––––––––––––––––––––––––––––
# Brute force: Approach: Search with Array

def countElements(arr):
    count = 0
    for x in arr:
        if x + 1 in arr:
            count += 1
    return count

arr = [1, 2, 3]
print(countElements(arr))
# Output: 2

"""
Time: O(n^2)
  - Outer loop iterates over all n elements: O(n).
  - 'x + 1 in arr' is a list lookup, which takes O(n) in the worst case.
  - Overall: O(n * n) = O(n^2) time.

Space: O(1)
  - Only a constant number of variables (count, x) are used.
  - No additional data structures.
  - Overall: O(1) space.

🔑 Key Difference: Set vs. List Lookup Complexity
    • Set lookup: O(1) on average — uses a hash table for near-instant access.

    • List lookup: O(n) — requires scanning elements sequentially until a match is found.

"""




# ––––––––––––––––––––––––––––––––––––––––––––––––
# Task: Count elements x in an array such that x + 1 is also in the array, counting duplicates separately.
# Example: arr = [1, 2, 2, 3] → Output = 3 (1 and both 2s are counted because 2 and 3 are in the array)
# Why: Practices hash set usage for efficient lookup to check for x + 1.

def countElements(arr):  # Example: arr = [1, 2, 2, 3]

    # 1️⃣ Create a hash set from the array
    # Convert arr to a set for O(1) lookup
    # Why? We need to quickly check if x + 1 exists in the array
    hash_set = set(arr)  # hash_set = {1, 2, 3}

    # 2️⃣ Initialize counter
    # Initialize count to track elements x where x + 1 is in the array
    # Why? We need to count each valid x, including duplicates
    count = 0  # count = 0

    # 3️⃣ Iterate through the array
    # Check each element to see if x + 1 exists in the hash set
    # Why? We need to count each x where x + 1 is present
    for x in arr:  # x takes values [1, 2, 2, 3]
        # --- Iteration 1: x = 1 ---
        # Check if x + 1 is in the hash set
        # Why? If x + 1 exists, x is a valid element to count
        if x + 1 in hash_set:  # x = 1, x + 1 = 2, hash_set = {1, 2, 3}, 2 in hash_set is True
            count += 1  # count = 0 + 1 = 1
        # After Iteration 1: count = 1

        # --- Iteration 2: x = 2 ---
        if x == 2 and count == 1:
            if x + 1 in hash_set:  # x = 2, x + 1 = 3, hash_set = {1, 2, 3}, 3 in hash_set is True
                count += 1  # count = 1 + 1 = 2
            # After Iteration 2: count = 2

        # --- Iteration 3: x = 2 ---
        if x == 2 and count == 2:
            if x + 1 in hash_set:  # x = 2, x + 1 = 3, hash_set = {1, 2, 3}, 3 in hash_set is True
                count += 1  # count = 2 + 1 = 3
            # After Iteration 3: count = 3

        # --- Iteration 4: x = 3 ---
        if x == 3:
            if x + 1 in hash_set:  # x = 3, x + 1 = 4, hash_set = {1, 2, 3}, 4 not in hash_set, False
                count += 1  # skip
            # After Iteration 4: count = 3

    # 4️⃣ Return the count
    # Why? count contains the number of elements x where x + 1 is in the array
    return count  # count = 3


arr = [1, 2, 2, 3]
print(countElements(arr))  # Output: 3