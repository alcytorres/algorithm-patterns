# Big Picture:
# - This code defines a doubly linked list, where each node holds a value, a link to the next node, and a link to the previous node.
# - It creates a list: 3 <-> 1 <-> 7.
# - Three functions: insert_at_beginning adds a node at the start, insert_at_end adds a node at the end, and display shows the list as a string.
# - Insertions are O(1) as they update pointers directly; display is O(n) as it traverses the list.

# The 'next' and 'prev' in DoublyNode are unrelated to the next() iterator function; they are just naming conventions.
# They refer to the next and previous nodes in the doubly linked list, not iteration.

# Class definition for a node in a doubly linked list
class DoublyNode:
    def __init__(self, value, next=None, prev=None):
    # Initializes node with value, next (default None), and prev (default None).
    # self: The node. value: Data. next: Link to next node. prev: Link to previous node.
        self.value = value
        # Sets node’s value (e.g., 1).
        self.next = next
        # Sets link to next node or None.
        self.prev = prev
        # Sets link to previous node or None.

    def __str__(self):
    # Returns node’s value as string for printing.
        return str(self.value)
        # Converts value to string (e.g., "1").

# Create a doubly linked list: 3 <-> 1 <-> 7
# Creates a single node with value 1, next=None, prev=None.
# Both head and tail point to this node initially.
head = tail = DoublyNode(1)
    # - DoublyNode(1): Calls __init__(1, next=None, prev=None), so head.value = 1, head.next = None, head.prev = None.
    # - head = tail = this node, as it’s the only node.

# Each node has three things:
    # value: The data it holds (like 1, 3, or 7).
    # next: A slot to point to the next node (or None if it’s the last node).
    # prev: A slot to point to the previous node (or None if it’s the first node).

# Why the Syntax head.next and head.prev?
    # The . (dot) accesses a node’s attributes (like value, next, or prev).
    # head.next means “Look at the next slot of the head node.”
    # head.prev means “Look at the prev slot of the head node.”
    # head.next = node means “Put node into head’s next slot.”

# Insert at beginning: O(1)
# - Defines a function to add a new node at the start of the list.
# - head: Current head node (or None if empty). tail: Current tail node (or None if empty).
# - value: The value for the new node (e.g., 3).
def insert_at_beginning(head, tail, value):
# Adds node with value at start. O(1) time.
    new_node = DoublyNode(value, next=head)
    # Creates new node with value, next points to current head.
    if head:
        head.prev = new_node
        # If head exists, its prev points back to new node.
    head = new_node
    # Updates head to new node.
    if not tail:
        tail = new_node
        # If list was empty, tail is also new node.
    return head, tail
    # Returns updated head and tail.

# Insert at end: O(1)
# - Defines a function to add a new node at the end of the list.
# - head: Current head node (or None if empty). tail: Current tail node (or None if empty).
# - value: The value for the new node (e.g., 7).
def insert_at_end(head, tail, value):
# Adds node with value at end. O(1) time.
    new_node = DoublyNode(value, prev=tail)
    # Creates new node with value, prev points to current tail.
    if tail:
        tail.next = new_node
        # If tail exists, its next points to new node.
    tail = new_node
    # Updates tail to new node.
    if not head:
        head = new_node
        # If list was empty, head is also new node.
    return head, tail
    # Returns updated head and tail.

# Display list as string (e.g., "3 <-> 1 <-> 7"): O(n)
# - Defines a function to show the list as a string (e.g., "3 <-> 1 <-> 7").
# - head: The starting node of the list.
def display(head):
# Shows list as string (e.g., "3 <-> 1 <-> 7"). O(n) time.
    elements = []
    # Creates list to store values as strings.
    curr = head
    # Starts at head node.
    while curr:
    # Loops until curr is None.
        elements.append(str(curr.value))
        # Adds node’s value as string.
        curr = curr.next
        # Moves to next node.
    print(" <-> ".join(elements))
    # Prints values joined by " <-> ".

# Example Usage
# - Starts with: 1 (head and tail are the same node).
head, tail = insert_at_beginning(head, tail, 3)
    # - Adds node with value 3 at start.
    # - New list: 3 <-> 1.
    # - head points to node(3), tail points to node(1).
display(head)
    # - Prints: 3 <-> 1.
head, tail = insert_at_end(head, tail, 7)
    # - Adds node with value 7 at end.
    # - New list: 3 <-> 1 <-> 7.
    # - head points to node(3), tail points to node(7).
display(head)
    # - Prints: 3 <-> 1 <-> 7.

# To see the list, you could print values by following next pointers:
current = head
while current is not None:
    print(current.value)  # Prints 3, 1, 7
    current = current.next
# It’s like walking through the chain forward, printing each node’s value until the end.
# You could also traverse backward from tail:
current = tail
while current is not None:
    print(current.value)  # Prints 7, 1, 3
    current = current.prev
# Walks backward using prev pointers.

# Time and Space Complexity:
# - insert_at_beginning: O(1) time (updates pointers directly), O(1) space (one new node).
# - insert_at_end: O(1) time (updates pointers directly), O(1) space (one new node).
# - display: O(n) time (visits n nodes), O(n) space (stores n values in elements).

# Running the Code:
# - Save this in a file (e.g., doubly_linked_list.py).
# - Run: python doubly_linked_list.py
# - Output:
#   3 <-> 1
#   3 <-> 1 <-> 7

