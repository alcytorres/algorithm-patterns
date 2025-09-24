# 2342. Max Sum of a Pair With Equal Sum of Digits
    # SKIP UNTIL HEAP (Priority Queue) CHAPTER

# You are given a 0-indexed array nums consisting of positive integers. You can choose two indices i and j, such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].

# Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions. If no such pair of indices exists, return -1.

# Example 1:
    # Input: nums = [18, 43, 36, 13, 7]
    # Output: 54

    # Explanation: The pairs (i, j) that satisfy the conditions are:
    #  (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
    #   (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
    #  So the maximum sum that we can obtain is 54.

# Example 2:
    # Input: nums = [10, 12, 19, 14]
    # Output: -1
    # Explanation: There are no two numbers that satisfy the conditions, so we return -1.

# Solution: https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/solutions/6389851/max-sum-of-a-pair-with-equal-sum-of-digits/








# –––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown







# –––––––––––––––––––––––––––––––––––––––––––––––––
# Brute force 





# –––––––––––––––––––––––––––––––––––––––––––––––––
# Alternate Solution


def maximumSum(nums):
    def sd(x):
        s = 0
        while x:
            s += x % 10
            x //= 10
        return s

    best = {}
    ans = -1

    for x in nums:
        k = sd(x)
        if k in best:
            ans = max(ans, best[k] + x)
            if x > best[k]:
                best[k] = x
        else:
            best[k] = x

    return ans

nums = [18, 43, 36, 13, 7]
print(maximumSum(nums))
# Output: 54



# –––––––––––––––––––––––––––––––––––––––––––––––––
def maximumSum(nums):
    mp = [-1] * 82  # Fixed size array
    ans = -1

    for num in nums:
        digit_sum = sum(int(d) for d in str(num))

        if mp[digit_sum] != -1:
            ans = max(ans, num + mp[digit_sum])

        mp[digit_sum] = max(mp[digit_sum], num)

    return ans

nums = [18, 43, 36, 13, 7]
print(maximumSum(nums))
# Output: 54

# Time: O(n) (One pass through nums)
# Space: O(1) (Fixed array of size 82)



# –––––––––––––––––––––––––––––––––––––––––––––––––
