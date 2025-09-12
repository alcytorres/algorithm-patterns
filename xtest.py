from collections import defaultdict

def findMaxLength(nums):
    # Step 1: Initialize variables
    counts = defaultdict(int)
    counts[0] = -1
    diff = 0
    ans = 0 
    
    # Step 2: Process each number
    for i, num in enumerate(nums):
        if num == 1:
            diff += 1
        else:
            diff -= 1
        
        if diff in counts:
            ans = max(ans, i - counts[diff])
        else:
            counts[diff] = i  
    
    return ans


nums = [0, 1, 1, 1, 1, 1, 0, 0, 0]
print(findMaxLength(nums))
# Output: 6