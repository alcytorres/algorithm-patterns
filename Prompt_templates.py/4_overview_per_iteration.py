"""
============================================
OVERVIEW FOR EACH ITERATION TEMPLATE
============================================
"""
# I want you to create a compact, easy-to-follow iteration overview table for this LeetCode solution, exactly in the style I've been using in our previous chat.

# Use this format:

"""
Overview for Each Iteration
Input: {{input values / parameters}}

{{short description of what the algorithm is doing}}

i | {{most important variable 1}} | {{most important variable 2}} | {{most important variable 3 or condition}} | Action / Decision | {{state / result / array / stack / etc after this step}}
--|-------------------------------|-------------------------------|-------------------------------------|-------------------|------------------------------------------------------
{{rows...}}

Final: {{final answer / return value}}
"""

# Rules / preferences:
# - Keep tables narrow → use short column names (e.g. i instead of Iteration, l/r instead of left/right, etc.)
# - 4–6 columns maximum
# - Show important changes only (don't list every tiny detail)
# - Include the most useful state variable (array, stack, pointers, count, etc.) in the last column
# - If the loop has phases (like two-pointer compaction + zero-filling), label them clearly (Phase 1, Phase 2)
# - End with a one-line "Final:" summary
# - Make it compact and readable — avoid very long lines

# Code / problem to analyze:
# {{paste the full function code here}}

# Example input to trace (use this specific test case):
# {{paste the exact input you're interested in}}

# Please generate the overview table(s) using the format above.


# Example to reference: 

# 1133. Largest Unique Number
"""
Given an integer array nums, return the largest integer that only occurs once. If no integer occurs once, return -1.

Example:
    Input: nums = [1, 3, 9, 4, 9, 8, 3]
    Output: 8
    Explanation: The maximum integer in the array is 9 but it is repeated. The number 8 occurs only once, so it is the answer.


---
Overview for Each Iteration
Input: nums = [1, 3, 9, 4, 9, 8, 3]
Step 1: Count occurrences of each number
i  | num | counts
---|-----|---------------------------
-  | -   | {}
0  | 1   | {1:1}
1  | 3   | {1:1, 3:1}
2  | 9   | {1:1, 3:1, 9:1}
3  | 4   | {1:1, 3:1, 9:1, 41}
4  | 9   | {1:1, 3:1, 9:2, 4:1}
5  | 8   | {1:1, 3:1, 9:2, 4:1, 8:1}
6  | 3   | {1:1, 3:2, 9:2, 4:1, 8:1}

Step 2: Find largest number with count 1
num | counts[num] | max_unique
----|-------------|---------------------
-   | -           | -1
1   | 1           | 1 (1 > -1)
3   | 2           | 1 (skip, not unique)
9   | 2           | 1 (skip, not unique)
4   | 1           | 4 (4 > 1)
8   | 1           | 8 (8 > 4)

Final: 8

"""