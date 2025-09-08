# I need a super simple, easy to follow, beginner-friendly explanation of how this LeetCode solution works. Break it down into 4 main parts: "Most IMPORTANT thing to Understand", "Why this code Works, TLDR (why this code works in one sentence), and Quick Example Walkthrough.

# Make it crystal clear, focusing on why the code finds the correct answer for the given problem. I should be able to look back at this at any time and quickly follow along and understand it. 

# ⚠️ It is important you be concise and have no fluff in your reply. You should not sacrifice clarity, but if something can be said in fewer words without losing understanding, then use fewer words. This requires a delicate balance: always aim for maximum clarity with minimum words.

# Between each bullet point skip a line to space out the breakdown and make it more easy to scan

# Here is a great template with more detail of what I'm looking that you can you as a reference. While I want you to generanlly follow this template it is not rigit. If you think adding a little more detail to a specific problem is necessary for me to fully understand make sure to do that.

"""
Most IMPORTANT thing to Understand:
    • [Key intuition in 2–3 bullets — e.g., what the main variable tracks or what the core idea is]

    • [State the condition that guarantees we’ve found a valid answer, in plain words]

    • [If applicable, point out what the hash map / set / pointer is doing in simple terms]

Why this code Works:
    • Hash map / data structure role: [Explain what it stores and why it’s useful]

    • Prefix sum / sliding window / two pointers idea: [Explain how the technique applies here]

    • Efficiency: [1–2 bullets on why this avoids brute force, O(n) vs O(n^2)]

    • Intuition: [Beginner analogy — “like tallying votes”, “like keeping a running score”, etc.]

Quick Example Walkthrough:
    nums = [example input], k = [value if relevant]

    Step 1: [Describe what happens as you process elements one by one, how key variables (like curr, odd, counts, etc.) change]

    Step 2: [Show the subarrays / result as they’re discovered]

    Final Answer: [Result]
"""


# Example to reference: 
from collections import defaultdict

def largestUniqueNumber(nums):
    # Step 1: Count occurrences of each number
    counts = defaultdict(int)
    for num in nums:
        counts[num] += 1
    # Step 2: Find the largest number with count 1
    max_unique = -1
    for num in counts:
        if counts[num] == 1 and num > max_unique:
            max_unique = num
    return max_unique

nums = [1, 3, 9, 4, 9, 8, 3]
print(largestUniqueNumber(nums))
# Output: 8


# Example breakdown to reference: 
"""
Most IMPORTANT thing to Understand:
    • We need to find the largest number in the array that occurs exactly once.

    • First, we count how many times each number appears.

    • Then we check which numbers are unique (count == 1) and pick the largest one.

    • If no number is unique, we return -1.

Why this code Works:
    • Hash map (counts): stores how many times each number appears.

    • Scan through counts:
        • If a number's count == 1 → it's unique.
        • Compare with current max_unique and update if larger.

    • Efficiency: Instead of checking subarrays or sorting, we just tally counts in O(n) and then make one pass over the results.

    • Intuition: Think of it like a vote tally — each number “gets votes.” We only want numbers that got exactly one vote, and we pick the biggest of those.

TLDR
    • This solution works because we count how often each number appears, then pick the largest one that occurs exactly once.
    
Quick Example Walkthrough:
    nums = [1, 3, 9, 4, 9, 8, 3]

    Step 1: Count frequencies
        counts = {1:1, 3:2, 9:2, 4:1, 8:1}

    Step 2: Check unique numbers
        • 1 → count=1, max_unique = 1
        • 3 → count=2, skip
        • 9 → count=2, skip
        • 4 → count=1, max_unique = 4
        • 8 → count=1, max_unique = 8

    Final Answer: 8
"""


# Leetcode problem for you to breakdown















print(1%2)






# print(1//2)

# print(102//2)



# def fn(nums):
#     ans = {}
#     for i, num in enumerate(nums):
#         ans[i] = num
#     return ans
    
# nums = ['a', 'b', 'c']
# print(fn(nums))


# nums = ['a', 'b', 'c']
# for i, num in enumerate(nums):
#     print(i, num)  
# # Prints: 
# # 0 a
# # 1 b
# # 2 c


