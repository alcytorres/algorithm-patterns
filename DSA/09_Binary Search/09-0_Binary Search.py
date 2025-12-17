# ============================================================
# Binary Search
# ============================================================
"""
You should think about binary search anytime the input is SORTED.

Binary search runs in O(log n), which is extremely fast and often a huge optimization over linear scans.
"""

# ============================================================
# Standard Binary Search (MOST IMPORTANT — memorize this)
# ============================================================
"""
Use this when:
• You need to find the EXACT value
• Return index if found, else return -1 (or existence)
• Elements are DISTINCT, or duplicates don't matter

IMPORTANT:
• When the target is NOT found, `left` ends up at the insertion position.
• This is why this template ALSO works for insertion problems
  when values are distinct (ex: LeetCode 35).
"""

# Binary search Template
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    # Target not found
    # `left` is the correct insertion position
    return left   # or -1 depending on the problem

# ============================================================
# Lower Bound — Left-Most Insertion Point (for DUPLICATES)
# ============================================================
"""
Use this ONLY when:
• The array MAY contain duplicates
• The problem asks for:
    - "first occurrence"
    - "left-most index"
    - insertion position WHEN duplicates exist

Returns:
• The smallest index where arr[index] >= target
"""

def lower_bound(arr, target):
    left = 0
    right = len(arr)

    while left < right:
        mid = (left + right) // 2

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left

# ============================================================
# Upper Bound — Right-Most Insertion Point (for DUPLICATES)
# ============================================================
"""
Use this ONLY when:
• The array MAY contain duplicates
• The problem asks for:
    - "last occurrence"
    - "right-most index"
    - "count occurrences"

Returns:
• The smallest index where arr[index] > target
"""

def upper_bound(arr, target):
    left = 0
    right = len(arr)

    while left < right:
        mid = (left + right) // 2

        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid

    return left

# ============================================================
# How to Choose the RIGHT Binary Search (No Confusion)
# ============================================================

"""
ONE RULE TO REMEMBER:

• If values are DISTINCT → Standard Binary Search is enough
• If DUPLICATES matter → Use Lower / Upper Bound

Quick mapping:
• Exact index / exists?                → STANDARD
• Insert position (distinct values)    → STANDARD (return left)
• First occurrence                     → LOWER BOUND
• Last occurrence                      → UPPER BOUND
• Count occurrences                    → upper_bound - lower_bound

Examples:
• LeetCode 704 (Binary Search)          → STANDARD
• LeetCode 35 (Search Insert Position)  → STANDARD (distinct values)
• First/Last position problems          → LOWER / UPPER BOUND
"""
