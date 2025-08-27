





















# ––––––––––––––– Prompts –––––––––––––––
# Super simple, beginner-friendly Leetocde breakdown

# I need a super simple, beginner-friendly explanation of how this LeetCode solution works, as if explaining to a 12-year-old who’s just learning to code. Break it down crystal clear, focusing on why the code finds the correct answer for the given problem. 

# Use the provided example input and output to walk through the solution step by step, showing how each part of the code contributes to the final result. Include a simple analogy to make it relatable. If the solution uses a loop, provide a concise iteration overview (like a table) showing key variable changes for each step.



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