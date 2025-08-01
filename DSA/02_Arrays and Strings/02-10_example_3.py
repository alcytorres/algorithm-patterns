# Example 3: 713. Number of Subarrays with Product Less Than k
# Counts subarrays where product of elements is strictly less than k.
# Example
# nums = [2, 3], k = 7
# Output: 3 --> [2], [2, 3], [3]

# Solution: https://leetcode.com/problems/subarray-product-less-than-k/


def num_subarrays_product_less_than_k(nums, k):
    if k <= 1:     
        return 0
    
    left = ans = 0          
    curr = 1          
    
    for right in range(len(nums)):  
        curr *= nums[right]        
        
        while curr >= k:           
            curr //= nums[left]    
            left += 1           
            
        ans += right - left + 1  
    
    return ans

print(num_subarrays_product_less_than_k([10, 5, 2, 6], 100))  
# Output: 8
# [10]
# [10, 5]
# [5]
# [5, 2]
# [2]
# [5, 2, 6]
# [2, 6]
# [6]

# Time: O(n) - Right pointer moves n times, left pointer moves at most n times (amortized O(1) per iteration).
# Space: O(1) - Uses only three integer variables (left, curr, ans).


# Trace Steps
# right =  0  0   1   2       3
# curr  =  1  10  50  100 10  60
# left  =  0               1
# ans   =  0  1   3        5  8


# Super simple demo of sliding window with multiplication and division
nums = [2, 4, 5]  # Basic array
curr = 1          # Start with product = 1
print("Initial curr:", curr)  # Output: 1

# Add elements to window (multiply)
curr *= nums[0]   # Include nums[0] (2), curr = 1 * 2
print("After curr *= nums[0]:", curr)  # Output: 2
curr *= nums[1]   # Include nums[1] (4), curr = 2 * 4
print("After curr *= nums[1]:", curr)  # Output: 8
curr *= nums[2]   # Include nums[2] (5), curr = 8 * 5
print("After curr *= nums[2]:", curr)  # Output: 40

# Remove element from window (divide)
curr //= nums[0]   # Remove nums[0] (2), curr = 40 / 2
print("After curr //= nums[0]:", curr)  # Output: 20.0
curr //= nums[1]   # Remove nums[1] (4), curr = 20 / 4
print("After curr //= nums[1]:", curr)  # Output: 5.0


# Why is left += 1 inside of if curr >= k:?
    # left += 1 is inside if curr >= k: to slide the window only when the product exceeds k, ensuring the window stays valid by removing the leftmost element only when needed.

# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown
def num_subarrays_product_less_than_k(nums, k):
    if k <= 1:     # If k <= 1, no valid subarrays possible (since nums are positive)
        return 0
    
    left = 0       # Left bound of the window
    curr = 1       # Tracks product of current window
    ans = 0        # Tracks number of valid subarrays
    
    for right in range(len(nums)):  # Iterate right pointer over array
        curr *= nums[right]         # Multiply element to window product
        
        while curr >= k:           # Shrink window while product is >= k
            curr //= nums[left]    # Divide out leftmost element. 
            left += 1              # Move left pointer forward
            
        ans += right - left + 1  # Add number of valid subarrays ending at right
    
    return ans  # Returns the count of valid subarrays


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Task: Count the number of contiguous subarrays with a product strictly less than k.
# Assume nums contains positive integers.
# Example: nums = [10, 5, 2, 6], k = 100 → Output = 8 (subarrays: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6])
# Why: Practices sliding window technique to count subarrays meeting a product constraint.

def num_subarrays_product_less_than_k(nums, k):  # Example: nums = [10, 5, 2, 6], k = 100

    # 1️⃣ Input Validation
    # If k <= 1, return 0 since no subarray of positive integers can have product < k
    # Why? Positive integers have products >= 1, so no valid subarrays exist for k <= 1
    if k <= 1:  # k = 100, 100 <= 1 is false, proceed
        return 0  # skip

    # 2️⃣ Initialize variables
    # Initialize left pointer for the sliding window
    # Why? We use left to shrink the window when the product is too large
    left = 0  # left = 0

    # Initialize current product of the window
    # Why? We track the product of elements in the current window
    curr = 1  # curr = 1 (initial value for multiplication)

    # Initialize answer to count valid subarrays
    # Why? We need to track the number of subarrays with product < k
    ans = 0  # ans = 0

    # 3️⃣ Iterate with right pointer
    # Loop through the array with right pointer to expand the window
    # Why? We process each element to build windows and count valid subarrays
    for right in range(len(nums)):  # right goes from 0 to 3 (len(nums) = 4)
        # --- Iteration 1: right = 0 ---
        # Multiply the current element into the window product
        # Why? We expand the window by including the new element
        curr *= nums[right]  # nums[0] = 10, curr = 1 * 10 = 10

        # Shrink window while product is >= k
        # Why? We need the product to be < k for valid subarrays
        while curr >= k:  # curr = 10, k = 100, 10 >= 100 is false, skip
            curr //= nums[left]  # skip
            left += 1  # skip
        # Add the number of valid subarrays ending at right
        # Why? Each window from left to right is valid, and there are right - left + 1 subarrays
        ans += right - left + 1  # right = 0, left = 0, ans = 0 + (0 - 0 + 1) = 1
        # After Iteration 1: left = 0, curr = 10, ans = 1
        # Current window: [10] (product = 10, subarrays: [10])

        # --- Iteration 2: right = 1 ---
        if right == 1:
            curr *= nums[right]  # nums[1] = 5, curr = 10 * 5 = 50
            while curr >= k:  # curr = 50, k = 100, 50 >= 100 is false, skip
                curr //= nums[left]
                left += 1
            ans += right - left + 1  # right = 1, left = 0, ans = 1 + (1 - 0 + 1) = 3
            # After Iteration 2: left = 0, curr = 50, ans = 3
            # Current window: [10, 5] (product = 50, subarrays: [10], [5], [10, 5])

        # --- Iteration 3: right = 2 ---
        if right == 2:
            curr *= nums[right]  # nums[2] = 2, curr = 50 * 2 = 100
            while curr >= k:  # curr = 100, k = 100, 100 >= 100 is true
                curr //= nums[left]  # nums[0] = 10, curr = 100 // 10 = 10
                left += 1  # left = 0 + 1 = 1
                # Check again: curr = 10, k = 100, 10 >= 100 is false, exit while
            ans += right - left + 1  # right = 2, left = 1, ans = 3 + (2 - 1 + 1) = 5
            # After Iteration 3: left = 1, curr = 10, ans = 5
            # Current window: [5, 2] (product = 10, subarrays: [5], [5, 2])

        # --- Iteration 4: right = 3 ---
        if right == 3:
            curr *= nums[right]  # nums[3] = 6, curr = 10 * 6 = 60
            while curr >= k:  # curr = 60, k = 100, 60 >= 100 is false, skip
                curr //= nums[left]
                left += 1
            ans += right - left + 1  # right = 3, left = 1, ans = 5 + (3 - 1 + 1) = 8
            # After Iteration 4: left = 1, curr = 60, ans = 8
            # Current window: [5, 2, 6] (product = 60, subarrays: [6], [2, 6], [5, 2, 6])

    # 4️⃣ Return the count of valid subarrays
    # Why? ans contains the total number of subarrays with product < k
    return ans  # ans = 8


print(num_subarrays_product_less_than_k([10, 5, 2, 6], 100))
# Output: 8
# [10]
# [10, 5]
# [5]
# [5, 2]
# [2]
# [5, 2, 6]
# [2, 6]
# [6]