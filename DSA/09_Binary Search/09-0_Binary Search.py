

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