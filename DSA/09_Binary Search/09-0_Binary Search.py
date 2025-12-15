# Binary Search

You should think about binary search anytime the problem provides anything sorted. O(log n) is extremely fast and binary search is usually a huge optimization.


# Binary search Template
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            # do something
            return
        if arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    
    # target is not in arr, but left is at the insertion point
    return left


# ––––––––––––––––––––––––––––––––––––––––––––––
# Binary Search — Lower Bound (Left-Most Position in Duplicate Elements)
def binary_search(arr, target):
    left = 0
    right = len(arr)

    while left < right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            right = mid
        else:
            left = mid + 1

    return left

# ––––––––––––––––––––––––––––––––––––––––––––––
# Binary Search — Upper Bound (Right-Most Position in Duplicate Elements)
def binary_search(arr, target):
    left = 0
    right = len(arr)

    while left < right:
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid
        else:
            left = mid + 1

    return left



"""
Binary Search Templates — What to Memorize + When to Use Each

1) Standard Binary Search (MOST IMPORTANT — memorize this)
   Use when the problem says:
   • "Return the index if found, else -1"
   • Elements are unique OR you don't care which duplicate index you get
   • You only need exact match / existence

   Example: LeetCode 704 (unique elements, return index or -1) → use STANDARD.

2) Lower Bound (Left-Most Position)
   Use when the problem says:
   • "first occurrence" / "left-most index"
   • "insertion position" (where target should be inserted to keep sorted)

   Key condition:
   • if arr[mid] >= target: move right = mid

3) Upper Bound (Right-Most Position)
   Use when the problem says:
   • "last occurrence" / "right-most index"
   • "count occurrences" (often uses upper - lower)

   Key condition:
   • if arr[mid] > target: move right = mid

Quick Decision Rule (no overthinking):
   • Need exact index / exists? → STANDARD
   • Need first/left-most or insert spot? → LOWER BOUND
   • Need last/right-most or count? → UPPER BOUND
   
"""
