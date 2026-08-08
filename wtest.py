# Ask Claude, Grok, ChatGPT to name the top 50 most common DSA problems you rec I know.
# In the prompt find a way to include the ones you already have pracitced



# Organize mini guides doc. Delete the bottom part that says delete

# how do you know to do this ans = [0] * n   ?
# its not something intuitive. be realistic how you would think of that or if thats just comes down to memory?

# Review slicing arrays




#   a = (b × whole times) + leftover

# n % 10   # get the last digit
# n // 10  # remove the last digit



# What is point of this from typing import List

"""
Review common_algorithms.py 

Check on CLAUDE if the examples at the bottom of 09-0_Binary Search.py are worth knowing or if the 2 I practice are enough

Run operators.py guide through Claude to make it better? maybe more examples 
"""




# TODO: In 02-28_Intersection of Two Arrays.py — put the two-set solution at the top:
#   seen1 = set(nums1), seen2 = set(nums2), then for num in seen2: if num in seen1: ans.append(num)
# Keep lookup+seen second as the transferable pattern. Don't delete any solutions.

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ans = []
        seen1 = set(nums1)
        seen2 = set(nums2)
        
        for num in seen2:
            if num in seen1:
                ans.append(num)
        
        return ans

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

solution = Solution()
print(solution.intersection(nums1, nums2))
# Output: [2]

