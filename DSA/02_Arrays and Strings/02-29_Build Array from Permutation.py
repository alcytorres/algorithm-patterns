# 1920. Build Array from Permutation
"""
Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.

A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).
 
Example 1:
    Input: nums = [2, 0, 1]
    Output: [1, 2, 0]

    Explanation: The array ans is built as follows:
    ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]]]
        = [nums[2], nums[0], nums[1]]
        = [1, 2, 0]

Example 2:

Constraints:
    1 <= nums.length <= 1000
    0 <= nums[i] < nums.length
    The elements in nums are distinct.
 
Follow-up: Can you solve it without using an extra space (i.e., O(1) memory)?

Solution: https://leetcode.com/problems/build-array-from-permutation/description/
"""

# Solution: Direct loop + new output array
def buildArray(nums):
    ans = []

    for i in range(len(nums)):
        ans.append(nums[nums[i]])

    return ans

nums = [2, 0, 1]
print(buildArray(nums))
# Output: [1, 2, 0]


# ––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown
def buildArray(nums):
    ans = []              # Empty list to store the final answer

    for i in range(len(nums)):     # Go through each index position
        ans.append(nums[nums[i]])  # Look up index i, then look up that spot again

    return ans            # Return the built answer array


"""
Time: O(N)
  - Let N = length of nums.
  - One loop goes through each index from 0 to N - 1 → O(N).
  - Each iteration does two array lookups and one append → O(1) per index.
  - Overall: O(N).

Space: O(N)
  - The answer list ans stores N elements.
  - Only one loop variable i is used besides that.
  - Overall: O(N).


Interview Answer: Worst Case

Time: O(N)
  - Single pass through all N indices.
  - Each step is a constant-time lookup and append.

Space: O(N)
  - Output array ans holds N elements.
"""


"""
---
Most IMPORTANT thing to Understand:
    • For each index i, the answer is NOT nums[i] — it is nums[nums[i]].

    • nums[i] gives you another index inside the same array.

    • You use that second index to grab the actual value that goes into ans.

    • The loop builds one answer slot at a time, left to right.

---
Why this code Works:
    • Direct formula:
        • The problem literally says ans[i] = nums[nums[i]].
        • The code does exactly that for every index.

    • Two-step lookup per index:
        • Step 1: nums[i] tells you where to look next.
        • Step 2: nums[nums[i]] gives you the value to store.

    • Efficiency:
        • One pass through all N indices.
        • Each lookup and append is O(1).
        • Time: O(N). Space: O(N) for the output list.

    • Intuition:
        • Think of nums as a map of directions.
        • At each position i, nums[i] says "go look over there."
        • Whatever you find at that spot becomes your answer.

---
TLDR:
    • This works because it loops through every index and directly applies the rule ans[i] = nums[nums[i]], building the answer one slot at a time.


---
Quick Example Walkthrough:
    nums = [2, 0, 1]

    Step 1: Start with an empty answer list
        ans = []

    Step 2: Build each answer slot
        • i=0 → nums[0]=2 → nums[2]=1 → ans = [1]
        • i=1 → nums[1]=0 → nums[0]=2 → ans = [1, 2]
        • i=2 → nums[2]=1 → nums[1]=0 → ans = [1, 2, 0]

    Final Answer: [1, 2, 0]


---
Full Example Walkthrough:
    nums = [2, 0, 1]

    Starting State:
        ans = []
        i = 0 (about to start loop)

    Loop Iteration 1:
        i = 0

        First lookup:
            nums[i] = nums[0] = 2

        Second lookup:
            nums[nums[i]] = nums[2] = 1

        Append to ans:
            ans = [1]

    --------------------------------------------------

    Loop Iteration 2:
        i = 1

        First lookup:
            nums[i] = nums[1] = 0

        Second lookup:
            nums[nums[i]] = nums[0] = 2

        Append to ans:
            ans = [1, 2]

    --------------------------------------------------

    Loop Iteration 3:
        i = 2

        First lookup:
            nums[i] = nums[2] = 1

        Second lookup:
            nums[nums[i]] = nums[1] = 0

        Append to ans:
            ans = [1, 2, 0]

    --------------------------------------------------

    Final Check:
        Loop finished — all indices processed.

        return ans → [1, 2, 0]
"""


"""
Overview for Each Iteration
Input: nums = [2, 0, 1]

For each index i, look up nums[i] to get a second index, then grab nums[nums[i]] and append it to ans.

i | nums[i] | nums[nums[i]] | Action        | ans
--|---------|---------------|---------------|----------
- | -       | -             | start         | []
0 | 2       | 1             | append 1      | [1]
1 | 0       | 2             | append 2      | [1, 2]
2 | 1       | 0             | append 0      | [1, 2, 0]

Final: [1, 2, 0]






Follow-up: Can you solve it without using an extra space (i.e., O(1) memory)?















---
🧠 First Time? Thoughts → Code

Read the problem (10 sec)
    • Build a new array where each slot follows: ans[i] = nums[nums[i]].

    • "Zero-based permutation" means every value in nums is a valid index (0 to N-1).

    • The example already shows the formula — this is mostly a direct translation problem.


Start naive (totally fine)
    • For each index i, grab nums[i] as a pointer, then look up the value at that spot.

    • Write it as two explicit steps: index_to_look_at = nums[i], then answer_value = nums[index_to_look_at].

    • Already O(N) — this problem doesn't need a slower brute force.


The one insight that unlocks the optimal code
    • The two steps are the same lookup written twice — you can chain them into nums[nums[i]].

    • Same logic, fewer lines. No new algorithm needed.

    • The whole problem is just: read the rule, write the rule.


Thought → line of code  (final solution)
    ans = []
    → need a place to collect each computed answer

    for i in range(len(nums)):
    → go through every index position once

    ans.append(nums[nums[i]])
    → collapsed the two-step lookup from naive: nums[i] is the pointer, nums[nums[i]] is the value

    return ans
    → bookkeeping — just return what we built


Memory hook (one sentence)
    • At each index, follow the pointer (nums[i]), then grab whatever lives there — write it as nums[nums[i]].


Would you arrive at this cold?
    • Immediately: loop through indices, build a new array, apply some rule per index.

    • The two-step version (pointer → value) is a natural first draft — same O(N), just more verbose.

    • Collapsing into nums[nums[i]] is how you land on the final solution — same logic, one expression.

    • ans = [] and return ans are bookkeeping; the real insight is ans.append(nums[nums[i]]).






---
Q: Why is append O(1) if array insertion is O(N)?

    • "Array insertion = O(N)" usually means inserting at an arbitrary index.

    Example:
        [1, 2, 3, 4]
        Insert 99 at index 1

        [1, 99, 2, 3, 4]

    • Elements must shift right to make room.
    • Shifting can take O(N) time.

--------------------------------------------------
append() is different:

    arr.append(x)

    [1, 2, 3]
             ↑
         add here

    [1, 2, 3, x]

    • No elements need to shift.
    • Usually takes O(1) time.

--------------------------------------------------
Technically:

    append() = O(1) amortized

    • Occasionally Python must resize the array.
    • That resize costs O(N).
    • But it happens rarely.

    Average cost per append:
        O(1)

--------------------------------------------------
For this problem:

    ans.append(nums[nums[i]])

    • append() → O(1) amortized
    • Runs N times

    Time Complexity:
        O(N)

    Space Complexity:
        O(N)
"""







# ––––––––––––––––––––––––––––––––––––––––––––––
# No Natural Brute Force Solution
"""
    • The problem gives the formula directly: ans[i] = nums[nums[i]]. There is no simpler approach with worse complexity.

    • Optimal complexity: Time O(N), Space O(N).

    • Any "two-step" version (index_to_look_at = nums[i], then nums[index_to_look_at]) is the same O(N) algorithm — just more verbose. Collapsing into nums[nums[i]] is a style change, not an optimization.

    • Recommendation: Focus on understanding the optimal solution clearly and move on.
"""










# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# My first attempt (before looking up the solution) — two explicit steps per index
# Valid & optimal — val = nums[i] then nums[val] is the same O(N) logic as nums[nums[i]]

class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        ans = []
        for i in range(len(nums)):
            val = nums[i]
            ans.append(nums[val])

        return ans

solution = Solution()
nums = [2, 0, 1]

print(solution.buildArray(nums))
# Output: [1, 2, 0]


# Overview
# ans[i] = nums[nums[i]]
# ans[0] = nums[nums[0]]
# ans[0] = nums[2]
# ans[0] = 1
# ans = [1]

# ans[i] = nums[nums[i]]
# ans[1] = nums[nums[1]]
# ans[1] = nums[0]
# ans[1] = 2
# ans = [1, 2]

# ans[i] = nums[nums[i]]
# ans[2] = nums[nums[2]]
# ans[2] = nums[1]
# ans[2] = 0
# ans = [1, 2, 0]