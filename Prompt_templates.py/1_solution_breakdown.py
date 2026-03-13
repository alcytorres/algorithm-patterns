"""
============================================
SOLUTION BREAKDOWN
============================================

Give me a breakdown of this LeetCode-style solution in the exact style I've been using in this chat.

Use this exact format and tone:

1. Start with this header line:
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

2. Then write "# Breakdown" on the next line

3. Then paste the full function code, but add a very short, natural-language comment (1-5 words) on almost every meaningful line, explaining what that line does in plain English (like a beginner-friendly notebook explanation).

4. Use very friendly, intuitive wording in comments (e.g. "Notebook to count…", "Go through each…", "Start with -1 because…", "Update to this bigger number", etc.)

5. Do NOT number the comments or make them too formal/technical.

6. Keep the code indentation and structure exactly the same.

7. Do NOT add time/space complexity or extra explanation blocks unless I specifically ask for them in this request.

Example of the style I want (use this layout and comment style):

"""


# Example of the style I want (use this layout and comment style):

# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown 
from collections import defaultdict

def largestUniqueNumber(nums):
    counts = defaultdict(int)  # Notebook to count how many times each number appears
    for num in nums:          # Go through each number in the list
        counts[num] += 1      # Add 1 to the count of this number in the notebook
    
    max_unique = -1           # Start with -1 (return this if no number appears once)
    for num in counts:        # Check each number in the notebook
        if counts[num] == 1 and num > max_unique:  # If number appears once and is bigger
            max_unique = num  # Update to this bigger number
    
    return max_unique         # Return the biggest number that appears once

