from collections import defaultdict

def findMaxLength(nums):
    # Step 1: Initialize variables
    counts = defaultdict(int)
    counts[0] = -1            
    diff = 0                 
    max_length = 0        
    
    # Step 2: Process each number
    for i, num in enumerate(nums):
        if num == 1:
            diff += 1         # Add 1 for a 1
        else:
            diff -= 1         # Subtract 1 for a 0
        if diff in counts:    
            max_length = max(max_length, i - counts[diff])  
        else:
            counts[diff] = i  
    
    return max_length


nums = [0, 1, 1, 1, 1, 1, 0, 0, 0]
print(findMaxLength(nums))


