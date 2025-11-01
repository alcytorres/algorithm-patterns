# Array Manipulation: Find max and min
"""
Task: Find the maximum and minimum elements in an array.

Example 1: [1, 2, 3] → Max: 3, Min: 1
Example 2: [4, 2, 5, 1] → Max: 5, Min: 1

Why: Introduces basic traversal and comparison in arrays.
"""

def find_max_min(arr):
    # 1️⃣ Handle edge case: empty array
    if not arr:
        return None, None
    
    # 2️⃣ Initialize max and min with the first element
    max_val = arr[0]
    min_val = arr[0]
    
    # 3️⃣ Traverse the array once, updating max and min as needed
    for num in arr:
        if num > max_val:
            max_val = num  # Update max if current number is larger
        if num < min_val:
            min_val = num  # Update min if current number is smaller
    
    # 4️⃣ Return the tuple of max and min values
    return max_val, min_val

print(find_max_min([1, 2, 3]))      # Output: (3, 1)
print(find_max_min([4, 2, 5, 1]))  # Output: (5, 1)


# Simple Breakdown
"""
Finds the maximum and minimum elements in an array.
- Traverses the array once, comparing each element to current max and min.
- Time Complexity: O(n), Space Complexity: O(1).
- Beginner-friendly single-pass solution.
"""