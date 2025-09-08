





















# ––––––––––––––– Prompts –––––––––––––––
# Super simple, beginner-friendly Leetocde FULL breakdown

# I need a super simple, beginner-friendly explanation of how this LeetCode solution works, as if explaining to a 12-year-old who’s just learning to code. Break it down crystal clear, focusing on why the code finds the correct answer for the given problem. 

# Use the provided example input and output to walk through the solution step by step, showing how each part of the code contributes to the final result. Include a simple analogy to make it relatable. If the solution uses a loop, provide a concise iteration overview (like a table) showing key variable changes for each step.



# ––––––––––––––––––––––––––––
# I need a super simple, easy to follow, beginner-friendly explanation of how this LeetCode solution works. Break it down into 2 main parts: "Most IMPORTANT thing to Understand:" and "Why this code Works:. Make it crystal clear, focusing on why the code finds the correct answer for the given problem. I should be able to look back at this at any time and quckly follow along and understand it. 

# Here is a great example of what I'm looking for from another Leetcode problem that you can you as a reference. 

"""
Most IMPORTANT thing to Understand:
    • odd is like a running total of how many odd numbers we’ve seen so far.

    • If we’ve seen (odd - k) before, it means the subarray between that earlier point and now contains exactly k odd numbers.

    • counts[odd - k] tells us how many such earlier points exist, so we add that to ans.

Why this code Works:
    • Hash map: counts keeps track of how often each odd count has appeared.

    • Prefix sum idea: odd works like a prefix sum. A subarray has k odds when odd - prev = k, or equivalently prev = odd - k.

    • Efficiency: Instead of checking every subarray, we find valid ones in one pass using the hash map lookups.

    • Intuition: We’re keeping a running tally of odd numbers and “remembering” past tallies, so whenever the difference is k, we instantly know a subarray is valid.
"""


# –––––––––––––––––––––––––––––––––––––––––––––––
# What is the best simple solution, easy to follow for a beginner for this problem that is efficient? Justify your answer


# –––––––––––––––––––––––––––––––––––––––––––––––
# What is the best efficient simple solution for a beginner to understand this problem. Justify your answer

# The goal is clarity and learning for a beginner to easily follow along



# –––––––––––––––––––––––––––––––––––––––––––––––
# Give me time and space for the following in this format:
    # Format like this
    # Time: O(n)
    # - Loop through nums once: O(n) iterations.
    # - Dictionary lookups and updates ('counts[curr - k]', 'counts[curr] += 1') are O(1) on average.
    # - No nested loops, so total time is O(n).

    # Space: O(n)
    # - Dictionary 'counts' can store up to n different prefix sums in the worst case: O(n) space.
    # - A few variables (curr, ans, num) take O(1) space.
    # - Overall: O(n) total space.






# –––––––––––––––––––––––––––––––––––––––––––––––
# Give me the overview of each iteration of this code
# Provide your answer in a .py file so i can copy it into the write up for this problem
# Only reply with the Overview for Each Iteration


# Here is a great example.
# Note you can choose the format you think is best for the overview depending on the problem. You dont always have to do a 2 steps breakdown. In this example it just really made sense. 
# The goal is clarity and learning for a beginner to easily follow along


# from collections import defaultdict

# def largestUniqueNumber(nums):
#     # Step 1: Count occurrences of each number
#     counts = defaultdict(int)
#     for num in nums:
#         counts[num] += 1
    
#     # Step 2: Find the largest number with count 1
#     max_unique = -1
#     for num in counts:
#         if counts[num] == 1 and num > max_unique:
#             max_unique = num
    
#     return max_unique

# nums = [1, 3, 9, 4, 9, 8, 3]
# print(largestUniqueNumber(nums))
# Output: 8

# counts = {1:1, 3:2, 9:2, 4:1, 8:1}


# Overview for Each Iteration
# Step 1: Count occurrences
# Idx | num | counts
# -   | -   | {}
# 0   | 1   | {1:1}
# 1   | 3   | {1:1, 3:1}
# 2   | 9   | {1:1, 3:1, 9:1}
# 3   | 4   | {1:1, 3:1, 9:1, 4:1}
# 4   | 9   | {1:1, 3:1, 9:2, 4:1}
# 5   | 8   | {1:1, 3:1, 9:2, 4:1, 8:1}
# 6   | 3   | {1:1, 3:2, 9:2, 4:1, 8:1}

# Step 2: Find largest unique number
# num | counts[num] | max_unique
# -   | -           | -1
# 1   | 1           | 1 (updated)
# 3   | 2           | 1 (skipped)
# 9   | 2           | 1 (skipped)
# 4   | 1           | 4 (updated)
# 8   | 1           | 8 (updated)
# Final: 8







# –––––––––––––––––––––––––––––––––––––––––––––––
# Give me a excellent one sentence explanation of the output like this:
    # Output: 3.5  --> Subarray [3, 4] (length 2, sum 3 + 4 = 7, average 7/2 = 3.5) has the largest average for k=2.



# –––––––––––––––––––––––––––––––––––––––––––––––
# Give me excellent in line annotations for this code



# –––––––––––––––––––––––––––––––––––––––––––––––
# Prompt for Guides
# here is a guide based on sliding windows i have based on the section of my dsa course on sliding windows

# give me a guide now for prefix sum that follows the format of the sliding window guide exactly in terms of spacing / format/ etc. Im going to copy and paste your answer into a .py file

# Use of lines to separate example problems

# as you will notice my guide is almost entirely just based of the pseudocode and examples given
# you can include additional information. if you choose to do this include at a cheatsheet at the bottom of the guide after the examples and only include the absolute. most important info concisely in a simple excellent way for me to quickly understand the most important things you think i should have 




# –––––––––––––––––––––––––––––––––––––––––––––––


















# class DoublyNode:
#     def __init__(self, value, next=None, prev=None):
#         self.value = value
#         self.next = next
#         self.prev = prev

#     def __str__(self):
#         return str(self.value)

# # Display a doubly linked list as a string (e.g., '3 <-> 1 <-> 7'). O(n)
# def display(head):
#     if not head:
#         return "Empty List"
#     elements = []
#     curr = head
#     while curr:
#         elements.append(str(curr.value))
#         curr = curr.next
#     return " <-> ".join(elements)

# # Inserts a node at the beginning of a doubly linked list. O(1)
# def insert_at_beginning(head, tail, value):
#     new_node = DoublyNode(value)
#     if not head:  # Empty list
#         return new_node, new_node
#     new_node.next = head
#     head.prev = new_node
#     return new_node, tail

# # Inserts a node at the end of a doubly linked list. O(1)
# def insert_at_end(head, tail, value):
#     new_node = DoublyNode(value)
#     if not head:  # Empty list
#         return new_node, new_node
#     tail.next = new_node
#     new_node.prev = tail
#     return head, new_node


# # Example Usage

# # Creates single node with value 1 (head and tail are same).
# head = tail = DoublyNode(1)

# # Display initial list state
# print("Initial list:", display(head))  # Output: 1
# # Insert 3 at the beginning: 3 <-> 1
# head, tail = insert_at_beginning(head, tail, 3)
# print("After inserting 3 at beginning:", display(head))  # Output: 3 <-> 1
# # Insert 7 at the end: 3 <-> 1 <-> 7
# head, tail = insert_at_end(head, tail, 7)
# print("After inserting 7 at end:", display(head))  # Output: 3 <-> 1 <-> 7



# # ––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# # # Get List Length
# def get_length(head):
#     count = 0          # Initialize counter
#     curr = head        # Start at head
#     while curr:        # Traverse until None
#         count += 1     # Increment for each node
#         curr = curr.next  # Move to next node
#     return count       # Return total nodes

# # Test get_length
# print("List length:", get_length(head))  # Output: 3 (for 3 <-> 1 <-> 7)


# # ––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# # Check if Value Exists
# def has_value(head, value):
#     curr = head
#     while curr:
#         if curr.value == value:
#             return True
#         curr = curr.next
#     return False

# # Test has_value
# print("Has value 1:", has_value(head, 1))  # Output: True
# print("Has value 5:", has_value(head, 5))  # Output: False