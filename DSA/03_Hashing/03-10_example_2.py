# 2248. Intersection of Multiple Arrays

# Example 2: Given a 2D array nums that contains n arrays of distinct integers, return a sorted array containing all the numbers that appear in all n arrays.

# For example, given nums = [[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]], return [3, 4]. 3 and 4 are the only numbers that are in all arrays.

# Example:
    # Input: nums = [[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]
    # Output: [3, 4]
    # Explanation: The only integers present in each of:
        # nums[0] = [3, 1, 2, 4, 5], 
        # nums[1] = [1, 2, 3, 4], and 
        # nums[2] = [3, 4, 5, 6] 
        # are 3 and 4, so we return [3, 4].

# Solution: https://leetcode.com/problems/intersection-of-multiple-arrays/solutions/


# Import defaultdict for counting element occurrences
from collections import defaultdict

def intersection(nums):
    counts = defaultdict(int)
    
    # Count occurrences of each element in all arrays
    for arr in nums:
        for x in arr:
            counts[x] += 1

    # Get number of arrays
    n = len(nums)
    # Initialize result list for common elements
    ans = []
    
    # Collect elements appearing in all arrays (count equals number of arrays)
    for key in counts:
        if counts[key] == n:
            ans.append(key)
    
    # Return sorted list of common elements
    return sorted(ans)

nums = [[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]
print(intersection(nums))  
# Output: [3, 4]

# Output: [3, 4] → 3 and 4 are the only nums that appear in all three arrays.

# Counts = {3: 3, 1: 2, 2: 2, 4: 3, 5: 2, 6: 1}


"""
Time: O(T log T)
  - Let N = number of arrays, and T = total number of elements across all arrays.
  - Step 1: Count occurrences of all numbers → O(T).
      • Each element is processed once and added to dictionary in O(1) average.
  - Step 2: Iterate through dictionary keys → O(U), where U ≤ T.
      • Collect elements appearing in all N arrays → O(U).
  - Step 3: Sort final result → O(M log M), where M = number of common elements.
  - Overall: O(T + M log M).  
    - In worst case (many common elements), M ≤ T → O(T log T).

Space: O(U)
  - Dictionary 'counts' stores up to U unique numbers.
  - Result list 'ans' holds up to U elements.
  - A few scalar variables (n, key) use O(1).
  - Overall: O(U), worst case O(T).

  
Interview Answer: Worst Case

Time: O(T log T)
  - Count all elements once, sort final result.

Space: O(T)
  - Dictionary and result list store all unique elements.



Overview for Each Iteration
Input: nums = [[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]

Step 1: Count occurrences of each element across all arrays
arr_idx | arr         | x | counts
--------|-------------|---|--------------------------------
-       | -           | - | {}
0       | [3,1,2,4,5] | 3 | {3:1}
0       | [3,1,2,4,5] | 1 | {3:1, 1:1}
0       | [3,1,2,4,5] | 2 | {3:1, 1:1, 2:1}
0       | [3,1,2,4,5] | 4 | {3:1, 1:1, 2:1, 4:1}
0       | [3,1,2,4,5] | 5 | {3:1, 1:1, 2:1, 4:1, 5:1}
1       | [1,2,3,4]   | 1 | {3:1, 1:2, 2:1, 4:1, 5:1}
1       | [1,2,3,4]   | 2 | {3:1, 1:2, 2:2, 4:1, 5:1}
1       | [1,2,3,4]   | 3 | {3:2, 1:2, 2:2, 4:1, 5:1}
1       | [1,2,3,4]   | 4 | {3:2, 1:2, 2:2, 4:2, 5:1}
2       | [3,4,5,6]   | 3 | {3:3, 1:2, 2:2, 4:2, 5:1}
2       | [3,4,5,6]   | 4 | {3:3, 1:2, 2:2, 4:3, 5:1}
2       | [3,4,5,6]   | 5 | {3:3, 1:2, 2:2, 4:3, 5:2}
2       | [3,4,5,6]   | 6 | {3:3, 1:2, 2:2, 4:3, 5:2, 6:1}

Final counts after processing all arrays: 
{3:3, 1:2, 2:2, 4:3, 5:2, 6:1}

Step 2: Collect elements appearing in all arrays (count == n = 3)
key | counts[key] | counts[key] == n | ans
----|-------------|------------------|----
1   | 2           | False            | []
2   | 2           | False            | []
3   | 3           | True             | [3]
4   | 3           | True             | [3, 4]
5   | 2           | False            | [3, 4]
6   | 1           | False            | [3, 4]

Final: sorted([3, 4]) = [3, 4]


---
Most IMPORTANT thing to Understand:
    • We're counting how many arrays each number appears in.

    • A number belongs in the answer only if it shows up in all arrays.

    • We use a hash map (counts[x]) to track the appearance count for each number across arrays.

---
Why this code Works:
    • Hash map role: counts[x] accumulates how many arrays contained x.

    • Condition: after counting, any x with counts[x] == n (n = number of arrays) must be present in every array → include it.

    • Efficiency: one pass over all elements to count, one pass over keys to filter, then sort the result — no need to compare arrays over and over.  

---
TLDR:
    • Count appearances of each number across arrays and return the numbers whose count equals the number of arrays.

---
Quick Example Walkthrough:
    nums = [[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]

    Step 1 (count):
        • After all arrays → counts = {3:3, 1:2, 2:2, 4:3, 5:2, 6:1}

    Step 2 (filter + sort):
        • Keep keys with count == 3 → [3, 4]
        • Sorted result → [3, 4]

    Final Answer: [3, 4]    



---
Q: What would be time and space if we do NOT sort the final ans?

  • Time: O(T) — counting and collecting elements only (no sorting).

  • Space: O(T) — dictionary + result list for unique elements.

"""


# ––––––––––––––––––––––––––––––––––––––––––––––––
# Intersection of Arrays: Sorted vs Unsorted Result (Impact on Time Complexity)

from collections import defaultdict

def intersection(nums):
    counts = defaultdict(int)
    
    for arr in nums:
        for x in arr:
            counts[x] += 1

    n = len(nums)
    ans = []
    
    for key in counts:
        if counts[key] == n:
            ans.append(key)
    
    # Return list of common elements: NO SORTING 
    return ans

nums = [[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]
print(intersection(nums))  
# Output: [3, 4]

"""
Time: O(N)
  - Count occurrences: O(N), where N is the total number of elements across all arrays.
  - Loop through dictionary keys (U unique numbers): O(U), and U ≤ N.
  - No sorting here, so overall: O(N) time.

Space: O(U) ≈ O(N)
  - same as before

  
---
Q: Why was the original time complexity O(N + k log k), but now it's only O(N)?

A: Because of the sorting step in the earlier version:
   • return sorted(ans) sorts the intersection result.
   • Sorting k elements costs O(k log k).
   • That's why the total time was O(N + k log k).

In this new version:
   • We just return ans without sorting.
   • No k log k cost → only the counting and scanning remain.
   • Total time is O(N).

"""



# ––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown 
def intersection(nums):
    counts = defaultdict(int)  # Initialize dictionary for element frequencies
    for arr in nums:          # Iterate over each subarray
        for x in arr:         # Iterate over each element in subarray
            counts[x] += 1    # Increment count for current element
    n = len(nums)             # Number of subarrays
    ans = []                  # Initialize result list

    for key in counts:        # Iterate over unique elements
        if counts[key] == n:  # If element appears in all subarrays
            ans.append(key)   # Add element to result

    return sorted(ans)        # Return sorted list of common elements



# ––––––––––––––––––––––––––––––––––––––––––––––––
# Brute force
def intersection_bruteforce(nums):
    if not nums:
        return []
    
    ans = []

    # For each candidate in the first array, check presence in all others
    for x in nums[0]:
        in_all = True
        for arr in nums[1:]:
            if x not in arr:   # linear scan of each list
                in_all = False
                break
        if in_all:
            ans.append(x)

    return sorted(ans)

nums = [[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]
print(intersection_bruteforce(nums))
# Output: [3, 4]


"""
Time: O(n * m * k + r log r)
  - For each element x in the first array (n elements), check presence in each of the other m-1 arrays.
  - Each "x not in arr" is a linear scan up to k elements → O(k).
  - Total scanning: O(n * m * k).
  - Sorting the result list of size r adds O(r log r).
  - Overall: O(n * m * k + r log r) time.

Space: O(n)
  - Result list 'ans' can store up to n elements (all from the first array).
  - A few variables (x, in_all, arr) take O(1) space.
  - No extra data structures used.
  - Overall: O(n) space.


Overview for Each Iteration
Input: nums = [[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]
Step 1: Check each candidate from nums[0] for presence in all other arrays
x  | arr          | x in arr | in_all | ans
---|--------------|----------|--------|-------
3  | [1, 2, 3, 4] | True     | True   | []
3  | [3, 4, 5, 6] | True     | True   | [3]
1  | [1, 2, 3, 4] | True     | True   | [3]
1  | [3, 4, 5, 6] | False    | False  | [3]
2  | [1, 2, 3, 4] | True     | True   | [3]
2  | [3, 4, 5, 6] | False    | False  | [3]
4  | [1, 2, 3, 4] | True     | True   | [3]
4  | [3, 4, 5, 6] | True     | True   | [3, 4]
5  | [1, 2, 3, 4] | False    | False  | [3, 4]

Step 2: Sort result
Final: sorted([3, 4]) = [3, 4]

"""




# ––––––––––––––––––––––––––––––––––––––––––––––––
# Task: Given a 2D array of distinct integers, return a sorted array of numbers that appear in all arrays.
# Example: nums = [[3,1,2,4,5], [1,2,3,4], [3,4,5,6]] → Output = [3, 4] (3 and 4 appear in all arrays)
# Why: Practices hash map usage to count occurrences across multiple arrays.

from collections import defaultdict

def intersection(nums):  # Example: nums = [[3,1,2,4,5], [1,2,3,4], [3,4,5,6]]

    # 1️⃣ Count occurrences of each number
    # Initialize a defaultdict to store number counts across all arrays
    # Why? We need to track how many arrays each number appears in
    counts = defaultdict(int)  # counts = {}

    # Iterate through each array and its elements
    # Why? We count each number's occurrences across all arrays
    for arr in nums:  # arr takes values [[3,1,2,4,5], [1,2,3,4], [3,4,5,6]]
        # --- Iteration 1: arr = [3,1,2,4,5] ---
        for x in arr:  # x takes values [3, 1, 2, 4, 5]
            counts[x] += 1  # counts[3] = 1, counts[1] = 1, counts[2] = 1, counts[4] = 1, counts[5] = 1
        # After Iteration 1: counts = {3: 1, 1: 1, 2: 1, 4: 1, 5: 1}

        # --- Iteration 2: arr = [1,2,3,4] ---
        if arr == [1, 2, 3, 4]:
            for x in arr:  # x takes values [1, 2, 3, 4]
                counts[x] += 1  # counts[1] = 2, counts[2] = 2, counts[3] = 2, counts[4] = 2
            # After Iteration 2: counts = {3: 2, 1: 2, 2: 2, 4: 2, 5: 1}

        # --- Iteration 3: arr = [3,4,5,6] ---
        if arr == [3, 4, 5, 6]:
            for x in arr:  # x takes values [3, 4, 5, 6]
                counts[x] += 1  # counts[3] = 3, counts[4] = 3, counts[5] = 2, counts[6] = 1
            # After Iteration 3: counts = {3: 3, 1: 2, 2: 2, 4: 3, 5: 2, 6: 1}

    # 2️⃣ Identify numbers in all arrays
    # Get the number of arrays
    # Why? We need numbers that appear in all n arrays
    n = len(nums)  # n = 3

    # Initialize result list for numbers appearing in all arrays
    # Why? We collect numbers with count equal to n
    ans = []  # ans = []

    # Check each number in counts
    # Why? Numbers with count == n appear in all arrays
    for key in counts:  # key takes values [3, 1, 2, 4, 5, 6]
        if counts[key] == n:  # n = 3
            # --- Key = 3 ---
            if key == 3 and counts[key] == 3:  # counts[3] = 3, 3 == 3, True
                ans.append(key)  # ans = [3]
            # --- Key = 1 ---
            if key == 1 and counts[key] == 3:  # counts[1] = 2, 2 == 3, False, skip
                ans.append(key)
            # --- Key = 2 ---
            if key == 2 and counts[key] == 3:  # counts[2] = 2, 2 == 3, False, skip
                ans.append(key)
            # --- Key = 4 ---
            if key == 4 and counts[key] == 3:  # counts[4] = 3, 3 == 3, True
                ans.append(key)  # ans = [3, 4]
            # --- Key = 5 ---
            if key == 5 and counts[key] == 3:  # counts[5] = 2, 2 == 3, False, skip
                ans.append(key)
            # --- Key = 6 ---
            if key == 6 and counts[key] == 3:  # counts[6] = 1, 1 == 3, False, skip
                ans.append(key)
    # After loop: ans = [3, 4]

    # 3️⃣ Return sorted result
    # Sort the result list
    # Why? The problem requires the output to be sorted
    return sorted(ans)  # sorted([3, 4]) = [3, 4]


nums = [[3,1,2,4,5], [1,2,3,4], [3,4,5,6]]
print(intersection(nums))  
# Output: [3, 4]