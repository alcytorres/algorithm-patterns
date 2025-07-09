# Linked Lists - Singly & Doubly Linked
# DSA Course in Python Lecture 3
# Video: https://www.youtube.com/watch?v=dqLHTK7RuIo&list=PLKYEe2WisBTFEr6laH5bR2J19j7sl5O8R&index=4

# Overview
# --------
# This guide covers singly and doubly linked lists, their structure, operations, and Big O complexities.
# Big O notation measures the worst-case growth rate of an algorithm's time or space usage as input size (n) increases.
# Time Complexity: Number of operations relative to input size.
# Space Complexity: Amount of memory used relative to input size.
# We analyze the worst-case scenario, focusing on the dominant complexity term.

# ****Delete this later...
# Linked lists are an alternative ways to store data compared to an array
# Linked list do NOT have indices 
# Generally we are given the head to the linked list 
# To find the elments in the list you have to traverse the linked list.


# 1. Singly Linked Lists
# ----------------------
# Definition: A data structure where each node contains a value and a reference (pointer) to the next node, forming a chain.
#  A node is like an object
# Characteristics:
# - Non-contiguous memory: Nodes are stored at different memory addresses, unlike arrays.
# - Nodes have a value and a next pointer (None at the end, marking the list's end).
# - Head: Reference to the first node; no direct access to other nodes.
# - No indices: Must traverse from head to access elements.
# Example: Head -> 1 -> 2 -> 3 -> None

# Node Structure:
# - Class with value (e.g., integer) and next (reference to next node or None).
# - Can store any data type, but LeetCode problems often use numbers.

# Key Operations and Big O Complexities
# - Access (get node at position k): O(n) - Traverse from head to position.
# - Search (find value): O(n) - Scan entire list in worst case.
# - Insert at position k: O(n) - Traverse to position, adjust pointers.
# - Delete at position k: O(n) - Traverse to position, adjust pointers.
# - Insert at head: O(1) - Constant time, update head and next pointer.
# - Delete at head: O(1) - Constant time, update head to next node.
# - Length: O(n) - Traverse to count nodes (not stored as property).

# Limitations:
# - No direct access to nodes (unlike arrays' O(1) indexing).
# - Inefficient for random access or middle operations (O(n)).

# Code Example: Singly Linked List Node and Operations
class SinglyNode:
    def __init__(self, value, next=None):
        self.value = value  # Store the value (e.g., 1)
        self.next = next    # Reference to next node or None

    def __str__(self):
        return str(self.value)  # String representation of node value

# Create a singly linked list: 1 -> 3 -> 4 -> 7 -> None
head = SinglyNode(1)  # Head node
a = SinglyNode(3)
b = SinglyNode(4)
c = SinglyNode(7)

# Link nodes
head.next = a  
a.next = b
b.next = c
# c.next is None by default

# Traverse and print: O(n)
def traverse_list(head):
    curr = head
    while curr:  # Until curr is None
        print(curr)  # Output: 1, 3, 4, 7
        curr = curr.next

# Display list as string (e.g., "1 -> 3 -> 4 -> 7"): O(n)
def display(head):
    elements = []
    curr = head
    while curr:
        elements.append(str(curr.value))
        curr = curr.next
    print(" -> ".join(elements))  # Glue elements with " -> "

# Search for value: O(n)
def search(head, value):
    curr = head
    while curr:
        if curr.value == value:
            return True
        curr = curr.next
    return False

# Example Usage
traverse_list(head)  # Output: 1, 3, 4, 7
display(head)        # Output: 1 -> 3 -> 4 -> 7
print(search(head, 2))  # Output: False (2 not in list)
print(search(head, 7))  # Output: True (7 in list)


# 2. Doubly Linked Lists
# ----------------------
# Definition: A data structure where each node contains a value, a next pointer, and a previous pointer, allowing traversal in both directions.
# Characteristics:
# - Non-contiguous memory, like singly linked lists.
# - Nodes have value, next, and prev pointers (None at head's prev and tail's next).
# - Head: First node; Tail: Last node, for efficient end operations.
# Example: None <- 1 <-> 2 <-> 3 -> None

# Node Structure:
# - Class with value, next (to next node or None), and prev (to previous node or None).

# Key Operations and Big O Complexities
# - Access (get node at position k): O(n) - Traverse from head or tail.
# - Search (find value): O(n) - Scan entire list.
# - Insert at position k: O(n) - Traverse to position, adjust pointers.
# - Delete at position k: O(n) - Traverse to position, adjust pointers.
# - Insert at head: O(1) - Constant time, update head and pointers.
# - Delete at head: O(1) - Constant time, update head.
# - Insert at tail: O(1) - Constant time, update tail and pointers.
# - Delete at tail: O(1) - Constant time, update tail.
# - Delete given node reference: O(1) - Constant time, adjust adjacent pointers.
# - Length: O(n) - Traverse to count nodes.

# Advantages:
# - Bidirectional traversal.
# - Efficient head/tail operations (O(1)).
# - Constant-time deletion with node reference (unlike singly linked lists).

# Doubly Linked List Node and Operations
class DoublyNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value  # Store the value
        self.next = next    # Reference to next node or None
        self.prev = prev    # Reference to previous node or None

    def __str__(self):
        return str(self.value)  # String representation of node value

# Display a doubly linked list as a string (e.g., '3 <-> 1 <-> 7'). O(n)
def display(head):
    if not head:
        return "Empty List"
    elements = []
    curr = head
    while curr:
        elements.append(str(curr.value))
        curr = curr.next
    return " <-> ".join(elements)

# Inserts a node at the beginning of a doubly linked list. O(1)
def insert_at_beginning(head, tail, value):
    new_node = DoublyNode(value)
    if not head:  # Empty list
        return new_node, new_node
    new_node.next = head
    head.prev = new_node
    return new_node, tail

# Inserts a node at the end of a doubly linked list. O(1)
def insert_at_end(head, tail, value):
    new_node = DoublyNode(value)
    if not head:  # Empty list
        return new_node, new_node
    tail.next = new_node
    new_node.prev = tail
    return head, new_node


# Example Usage

# Creates single node with value 1 (head and tail are same).
head = tail = DoublyNode(1)

# Display initial list state
print("Initial list:", display(head))  # Output: 1
# Insert 3 at the beginning: 3 <-> 1
head, tail = insert_at_beginning(head, tail, 3)
print("After inserting 3 at beginning:", display(head))  # Output: 3 <-> 1
# Insert 7 at the end: 3 <-> 1 <-> 7
head, tail = insert_at_end(head, tail, 7)
print("After inserting 7 at end:", display(head))  # Output: 3 <-> 1 <-> 7


# 3. Complexity Summary
# --------------------
# Singly Linked Lists:
# - Access: O(n)
# - Search: O(n)
# - Insert at position: O(n)
# - Delete at position: O(n)
# - Insert at head: O(1)
# - Delete at head: O(1)
# - Length: O(n)

# Doubly Linked Lists:
# - Access: O(n)
# - Search: O(n)
# - Insert at position: O(n)
# - Delete at position: O(n)
# - Insert at head: O(1)
# - Delete at head: O(1)
# - Insert at tail: O(1)
# - Delete at tail: O(1)
# - Delete with node reference: O(1)
# - Length: O(n)

# 4. Practical Insights
# ---------------------
# - Singly Linked Lists: Simple, memory-efficient (one pointer per node), but limited to forward traversal and inefficient for middle/end operations.
# - Doubly Linked Lists: More flexible with bidirectional traversal and O(1) tail operations, but use more memory (two pointers per node).
# - Use linked lists when frequent head/tail insertions/deletions are needed, not for random access (arrays are better for O(1) indexing).
# - Traversal is common in linked list problems; master pointer manipulation for LeetCode challenges.
# - Python’s references simplify pointer concepts compared to C, but understanding memory addresses is helpful.

# 5. Conclusion
# -------------
# Singly and doubly linked lists are dynamic data structures ideal for specific use cases like frequent head/tail modifications.
# Big O notation guides their efficiency, with O(1) operations at head/tail and O(n) for middle operations.
# Use this guide to implement linked lists in Python, understand their complexities, and prepare for algorithmic problems.

# Key Takeaways:
# - Linked lists use non-contiguous memory, unlike arrays.
# - Singly linked lists are simple but limited to forward traversal.
# - Doubly linked lists offer bidirectional traversal and O(1) deletion with node references.
# - Head/tail operations are O(1); middle operations are O(n).
# - Practice traversal and pointer adjustments for proficiency.

# End of Guide
# ------------
# Run the code examples in a Python environment (e.g., Colab) to experiment and deepen understanding.
# Colab notebook available in the video description: https://www.youtube.com/watch?v=dqLHTK7RuIo