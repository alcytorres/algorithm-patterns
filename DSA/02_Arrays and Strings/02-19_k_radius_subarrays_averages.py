# 2090. K Radius Subarray Averages

# Solution: https://leetcode.com/problems/k-radius-subarray-averages/description/

# Video https://www.youtube.com/watch?v=L33kbF6Cr_I

# Example
    # nums =  [7, 4, 3, 9, 1, 8, 5, 2, 6]
    # Output: [-1, -1, -1, 5, 4, 4, -1, -1, -1]

# Yashasvi Code: My Preferred solution
def getAverages(nums, k):
    n = len(nums)
    ans = [-1] * n
    window_size = 2*k + 1
    curr = 0

# Handle case where window can't fit in array
    if (n < window_size):
        return ans
 
# Calculate sum of the first full window 
    curr = sum(nums[0:window_size])
    ans[k] = curr // window_size
  
# Slide window across array and update averages
    for i in range(k+1, n-k): 
        curr += nums[i+k] - nums[i-k -1]
        ans[i] = curr // window_size

    return ans

nums = [7, 4, 3, 9, 1, 8, 5, 2, 6]
k = 3
print(getAverages(nums, k))
# Output: [-1, -1, -1, 5, 4, 4, -1, -1, -1]

# Time: O(n)
# - Create result array 'ans': O(n).
# - Compute first window sum: O(k).
# - Slide window across array: O(n) total, since each step adds one element and removes one element in O(1) time.
# - Overall time is O(n) because O(n) dominates O(k).

# Space: O(n)
# - Result array 'ans' takes O(n) space.
# - A few integer variables (n, window_size, curr_sum, i) take O(1) space.
# - Overall: O(n) total space.
# - If we exclude the result array from consideration, extra working space is O(1).



# Overview for Each Iteration
# Input: nums = [7, 4, 3, 9, 1, 8, 5, 2, 6], k = 3
# Step 1: Initialize variables
# n = 9, window_size = 2*3 + 1 = 7, ans = [-1, -1, -1, -1, -1, -1, -1, -1, -1]

# Step 2: Calculate sum of first full window (indices 0 to 6)
# curr = sum(nums[0:7]) = 7 + 4 + 3 + 9 + 1 + 8 + 5 = 37
# ans[3] = 37 // 7 = 5
# ans = [-1, -1, -1, 5, -1, -1, -1, -1, -1]

# Step 3: Slide window and compute averages
# i  | curr             | nums[i+k] | nums[i-k-1] | ans[i]    | ans
# 4  | 32 (37 + 2 - 7)  | 2         | 7           | 4 (32//7) | [-1, -1, -1, 5, 4, -1, -1, -1, -1]
# 5  | 34 (32 + 6 - 4)  | 6         | 4           | 4 (34//7) | [-1, -1, -1, 5, 4, 4, -1, -1, -1]
# Final: [-1, -1, -1, 5, 4, 4, -1, -1, -1]



# ––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown 
def getAverages(nums, k):
    n = len(nums)             # Length of input array
    ans = [-1] * n            # Initialize result array with -1
    window_size = 2*k + 1     # Size of k-radius window
    curr = 0                  # Initialize window sum

    if n < window_size:       # If array too small for window
        return ans            # Return array of -1s
    
    # Calculate sum of the first full window 
    curr = sum(nums[:window_size])  # Sum of first window
    ans[k] = curr // window_size    # Set average for first valid index

    # Slide window across array and update averages
    for i in range(k+1, n-k): # Slide window for remaining valid indices
        curr += nums[i+k] - nums[i-k-1]  # Update sum: add new, remove old
        ans[i] = curr // window_size     # Set average for current index

    return ans                # Return array of k-radius averages



# ––––––––––––––––––––––––––––––––––––––––––––––
# Task: Compute the k-radius subarray averages for each index i, where the average is of nums[i-k:i+k+1].
# If fewer than 2k+1 elements are available, return -1 for that index.
# Example: nums = [7, 4, 3, 9, 1, 8, 5, 2, 6], k = 3 → Output = [-1, -1, -1, 5, 4, 4, -1, -1, -1]
# Why: Practices sliding window technique to compute averages efficiently.

def getAverages(nums, k):  # Example: nums = [7, 4, 3, 9, 1, 8, 5, 2, 6], k = 3

    # 1️⃣ Initialize variables
    # Get the length of the input array
    # Why? We need the size to check window validity and create the result array
    n = len(nums)  # n = 9

    # Initialize result array with -1 for all indices
    # Why? Indices without a full window (2k+1 elements) get -1
    ans = [-1] * n  # ans = [-1, -1, -1, -1, -1, -1, -1, -1, -1]

    # Calculate window size (2k+1 for k elements on each side plus the center)
    # Why? Each average includes the center element and k elements on each side
    window_size = 2 * k + 1  # k = 3, window_size = 2 * 3 + 1 = 7

    # Initialize current sum for the sliding window
    # Why? We track the sum of the current window to compute averages
    curr = 0  # curr = 0

    # 2️⃣ Handle case where window can't fit in array
    # If array length is less than window size, return all -1s
    # Why? No index can have a full window if n < 2k+1
    if n < window_size:  # n = 9, window_size = 7, 9 < 7 is false, proceed
        return ans  # skip

    # 3️⃣ Calculate sum of the first full window
    # Sum the first 2k+1 elements (indices 0 to 6)
    # Why? We need the sum of the first window centered at index k
    curr = sum(nums[0:window_size])  # nums[0:7] = [7, 4, 3, 9, 1, 8, 5], curr = 7 + 4 + 3 + 9 + 1 + 8 + 5 = 37

    # Set the average for the first valid index (k)
    # Why? Index k is the center of the first window
    ans[k] = curr // window_size  # k = 3, curr = 37, window_size = 7, ans[3] = 37 // 7 = 5
    # After first window: ans = [-1, -1, -1, 5, -1, -1, -1, -1, -1]

    # 4️⃣ Slide window across array and update averages
    # Iterate from k+1 to n-k-1 to compute averages for valid centers
    # Why? Only indices from k to n-k-1 have full windows of size 2k+1
    for i in range(k + 1, n - k):  # k = 3, n = 9, i goes from 4 to 5
        # --- Iteration 1: i = 4 ---
        # Update sum: add element at i+k, subtract element at i-k-1
        # Why? This slides the window right, maintaining size 2k+1
        curr += nums[i + k] - nums[i - k - 1]  # i = 4, i+k = 4+3 = 7, i-k-1 = 4-3-1 = 0
                                                # nums[7] = 2, nums[0] = 7, curr = 37 + 2 - 7 = 32
        # Compute average and store in result
        ans[i] = curr // window_size  # curr = 32, window_size = 7, ans[4] = 32 // 7 = 4
        # After Iteration 1: curr = 32, ans = [-1, -1, -1, 5, 4, -1, -1, -1, -1]
        # Current window: [4, 3, 9, 1, 8, 5, 2] (sum = 32, indices 1 to 7)

        # --- Iteration 2: i = 5 ---
        if i == 5:
            curr += nums[i + k] - nums[i - k - 1]  # i = 5, i+k = 5+3 = 8, i-k-1 = 5-3-1 = 1
                                                    # nums[8] = 6, nums[1] = 4, curr = 32 + 6 - 4 = 34
            ans[i] = curr // window_size  # curr = 34, window_size = 7, ans[5] = 34 // 7 = 4
            # After Iteration 2: curr = 34, ans = [-1, -1, -1, 5, 4, 4, -1, -1, -1]
            # Current window: [3, 9, 1, 8, 5, 2, 6] (sum = 34, indices 2 to 8)

    # 5️⃣ Return the result
    # Why? ans contains the averages for valid indices and -1 for others
    return ans  # ans = [-1, -1, -1, 5, 4, 4, -1, -1, -1]


nums = [7, 4, 3, 9, 1, 8, 5, 2, 6]
print(getAverages(nums, 3))  # Output: [-1, -1, -1, 5, 4, 4, -1, -1, -1]






# ––––––––––––––––––––––––––––––––––––––––––––––
# Sliding Window Video Solution 2
# Video https://www.youtube.com/watch?v=L33kbF6Cr_I
    # I think I like this more than the LeetCode official solution
def getAverages(nums, k):
    left = 0
    window_size = 2*k + 1
    ans = [-1] * len(nums)
    total = 0

    for right, value in enumerate(nums):
        total += value
        #check that my window satisfies some condition
    
        if right - left + 1 == window_size:
            ans[left + k] = total // window_size
            #check to make sure that I have to move the left pointer
            total -= nums[left]
            left += 1
    
    return ans

nums = [7, 4, 3, 9, 1, 8, 5, 2, 6]
print(getAverages(nums, 3))
# Output: [-1, -1, -1, 5, 4, 4, -1, -1, -1]

# Time: O(n) – O(n) to create the result array, plus O(n) to slide the window (each element added and removed once).
# Space: O(n) total due to result array, O(1) auxiliary if excluding it.


# ––––––––––––––––––––––––––––––––––––––––––––––
# Sliding Window LeetCode Solution 3
# https://leetcode.com/problems/k-radius-subarray-averages/description/
def getAverages(nums, k):
    ans = [-1] * len(nums)
    if k == 0:
        return nums

    window_size = 2 * k + 1
    n = len(nums)

    if window_size > n:
        return ans

    # First get the sum of first window of the 'nums' arrray.
    window_sum = sum(nums[:window_size])
    ans[k] = window_sum // window_size

    # Iterate on rest indices which have at least 'k' elements 
    # on its left and right sides.
    for i in range(window_size, n):
        window_sum += nums[i] - nums[i - window_size]
        ans[i - k] = window_sum // window_size

    return ans

nums = [7, 4, 3, 9, 1, 8, 5, 2, 6]
print(getAverages(nums, 3))
# Output: [-1, -1, -1, 5, 4, 4, -1, -1, -1] - Returns averages of k-radius subarrays (k=3) where each valid index i has 2k+1 elements, else -1.

# Time: O(n) - Initializes averages array in O(n) and slides window over n elements with O(1) operations per iteration.
# Space: O(1) - Uses only a constant number of variables (window_sum, window_size), excluding the output array.


# ––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown 
# Sliding Window -> Makes more sense to me than prefix solution
def getAverages(nums, k):
    averages = [-1] * len(nums)
    # When a single element is considered then its average will be the number itself only.
    if k == 0:
        return nums

    window_size = 2 * k + 1
    n = len(nums)

    # Any index will not have 'k' elements in it's left and right.
    if window_size > n:
        return averages

    # First get the sum of first window of the 'nums' arrray.
    window_sum = sum(nums[:window_size])
    averages[k] = window_sum // window_size

    # Iterate on rest indices which have at least 'k' elements 
    # on its left and right sides.
    for i in range(window_size, n):
        # We remove the discarded element and add the new element to get current window sum.
        # 'i' is the index of new inserted element, and
        # 'i - (window size)' is the index of the last removed element.
        window_sum = window_sum - nums[i - window_size] + nums[i]
        averages[i - k] = window_sum // window_size

    return averages


# ––––––––––––––––––––––––––––––––––––––––––––––
# Prefix Sum Solution 4:
# https://leetcode.com/problems/k-radius-subarray-averages/description/

def getAverages(nums, k):
    # When a single element is considered then its average will be the number itself only.
    if k == 0:
        return nums

    window_size = 2 * k + 1
    n = len(nums)
    averages = [-1] * n

    # Any index will not have 'k' elements in it's left and right.
    if window_size > n:
        return averages

    # Generate 'prefix' array for 'nums'.
    # 'prefix[i + 1]' will be sum of all elements of 'nums' from index '0' to 'i'.
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]

    # We iterate only on those indices which have atleast 'k' elements in their left and right.
    # i.e. indices from 'k' to 'n - k'
    for i in range(k, n - k):
        leftBound, rightBound = i - k, i + k
        subArraySum = prefix[rightBound + 1] - prefix[leftBound]
        average = subArraySum // window_size
        averages[i] = average

    return averages

nums = [7, 4, 3, 9, 1, 8, 5, 2, 6]
print(getAverages(nums, 3))