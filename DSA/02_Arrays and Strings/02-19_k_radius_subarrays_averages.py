# 2090. K Radius Subarray Averages

# Solution: https://leetcode.com/problems/k-radius-subarray-averages/description/

# Video https://www.youtube.com/watch?v=L33kbF6Cr_I

# Eaxmple
# nums = [7, 4, 3, 9, 1, 8, 5, 2, 6]
# Output: [-1, -1, -1, 5, 4, 4, -1, -1, -1]


# Sliding Window Video Solution
# Video https://www.youtube.com/watch?v=L33kbF6Cr_I
    # I think I like this more than the LeetCode official solution
def getAverages(nums, k):
    left = 0
    window_size = 2*k + 1
    res = [-1] * len(nums)
    total = 0

    for right, value in enumerate(nums):
        total += value
        #check that my window satisfies some condition
    
        if right - left + 1 == window_size:
            res[left + k] = total // window_size
            #check to make sure that I have to move the left pointer
            total -= nums[left]
            left += 1
    
    return res

nums = [7,4,3,9,1,8,5,2,6]
print(getAverages(nums, 3))
# Output: [-1, -1, -1, 5, 4, 4, -1, -1, -1]

# Time: O(n) - Initializes averages array in O(n) and slides window over n elements with O(1) operations per iteration.
# Space: O(1) - Uses only a constant number of variables (window_sum, window_size), excluding the output array.



# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Sliding Window LeetCode Solution
def getAverages(nums, k):
    averages = [-1] * len(nums)
    if k == 0:
        return nums

    window_size = 2 * k + 1
    n = len(nums)

    if window_size > n:
        return averages

    # First get the sum of first window of the 'nums' arrray.
    window_sum = sum(nums[:window_size])
    averages[k] = window_sum // window_size

    # Iterate on rest indices which have at least 'k' elements 
    # on its left and right sides.
    for i in range(window_size, n):
        window_sum = window_sum - nums[i - window_size] + nums[i]
        averages[i - k] = window_sum // window_size

    return averages


nums = [7,4,3,9,1,8,5,2,6]
print(getAverages(nums, 3))
# Output: [-1, -1, -1, 5, 4, 4, -1, -1, -1] - Returns averages of k-radius subarrays (k=3) where each valid index i has 2k+1 elements, else -1.

# Time: O(n) - Initializes averages array in O(n) and slides window over n elements with O(1) operations per iteration.
# Space: O(1) - Uses only a constant number of variables (window_sum, window_size), excluding the output array.













# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
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



# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––



# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Prefix Sum Solution:

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

nums = [7,4,3,9,1,8,5,2,6]
print(getAverages(nums, 3))