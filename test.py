# 4. Find Pair with Target Difference
"""
Task: Find two numbers in an array whose difference is a given target. The larger number minus the smaller should equal the target. Return None if no pair is found.
Example 1: [1, 5, 4, 8], target = 3 → [1, 4]
Example 2: [1, 3, 8],    target = 2 → [1, 3]
Why: Prepares for Two Sum by practicing pointer movement for a condition.
"""

def find_pair_with_difference(arr, target):
    arr.sort()                   
    left, right = 0, 1           
    while right < len(arr):      
        diff = arr[right] - arr[left]  
        if diff == target:       
            return [arr[left], arr[right]]  
        elif diff < target:      
            right += 1           
        else:                   
            left += 1            
            if left == right:   
                right += 1       
    return None       

print(find_pair_with_difference([1, 4, 3, 7], 6))  # Output: [1, 7]
print(find_pair_with_difference([1, 3, 8], 2))  # Output: [1, 3]
print(find_pair_with_difference([8, 1, 3, 5], 3))  # Output: [5, 8]
print(find_pair_with_difference([1, 2, 10], 5))  # Output: None



