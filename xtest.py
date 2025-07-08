# Big Picture:
# - This code defines a singly linked list, where each node holds a value and a link to the next node.
# - It creates a list: 1 -> 3 -> 4 -> 7 -> None.
# - Three functions: traverse_list prints each node’s value, display shows the list as a string, and search checks if a value exists.
# - Each function iterates through the list, making them O(n) in time complexity.

# curr = current node

# The next in SinglyNode is unrelated to the next() iterator function; it’s just a naming coincidence. 
# It refers to the next node in the linked list, not iteration.


# Class definition for a node in a singly linked list
class SinglyNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)

# Create a singly linked list: 1 -> 3 -> 4 -> 7 -> None
head = SinglyNode(1)
a = SinglyNode(3)
b = SinglyNode(4)
c = SinglyNode(7)
head.next = a
a.next = b
b.next = c

# Traverse and print: O(n)
def traverse_list(head):
    curr = head
    while curr:
        print(curr)
        curr = curr.next

# Display list as string: O(n)
def display(head):
    elements = []
    curr = head
    while curr:
        elements.append(str(curr.value))
        curr = curr.next
    print(" -> ".join(elements))

# Search for value: O(n)
def search(head, value):
    curr = head
    while curr:
        if curr.value == value:
            return True
        curr = curr.next
    return False



# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Class definition for a node in a singly linked list
class SinglyNode:
    def __init__(self, value, next=None):
    # Initializes node with value and next (default None).
    # self: The node. value: Data. next: Link to next node.
        self.value = value
        # Sets node’s value (e.g., 1).
        self.next = next
        # Sets link to next node or None.

    def __str__(self):
    # Returns node’s value as string for printing.
        return str(self.value)
        # Converts value to string (e.g., "1").

# Create a singly linked list: 1 -> 3 -> 4 -> 7 -> None
# Creates head node with value 1, next=None.
head = SinglyNode(1)
    # - SinglyNode(1): Calls __init__(1, next=None), so head.value = 1, head.next = None.
# Creates node with value 3, next=None.
a = SinglyNode(3)
# Creates node with value 4, next=None.
b = SinglyNode(4)
# Creates node with value 7, next=None.
c = SinglyNode(7)

# Links head to a (1 -> 3).
head.next = a
    # - head.next: Sets head’s next to point to a (1 -> 3).
# Links a to b (3 -> 4).
a.next = b
# Links b to c (4 -> 7).
b.next = c
# c.next is None (end of list).
# c.next remains None, indicating the end of the list (7 -> None).

# Each node has two things:
    # value: The data it holds (like 1 or 3).
    # next: A slot to point to another node (or None if it’s the last node).

# Why the Syntax head.next?
    # The . (dot) is how you access a node’s attributes (like value or next).
    # head.next means “Look at the next slot of the head node.”
    # head.next = a means “Put the node a into head’s next slot.”

# To see the list, you could print the values by following the next pointers:
curr = head
while curr is not None:
    print(curr.value)  # Prints 1, 3, 4, 7
    curr = curr.next
# It’s like walking through the chain, printing each node’s value until the end.


# Traverse and print: O(n) 
# - Defines a function to print each node’s value in the list.
# - head: The starting node of the list (e.g., head with value 1).
def traverse_list(head):
    curr = head
    # Starts at head node.
    while curr:
    # Loops until curr is None.
        print(curr)
        # Prints node’s value (e.g., 1, 3, 4, 7).
        curr = curr.next
        # Moves to next node.

# Display list as string: O(n)
# - Defines a function to show the list as a string (e.g., "1 -> 3 -> 4 -> 7").
# - head: The starting node of the list.
def display(head):
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
    print(" -> ".join(elements))  # ['1', '3', '4', '7'] = '1 -> 3 -> 4 -> 7'
    # Prints values joined by " -> ".

# Search for value: O(n)
# - Defines a function to check if a value exists in the list.
# - head: The starting node.
# - value: The value to find (e.g., 2 or 7).
def search(head, value):
    curr = head
    # Starts at head node.
    while curr:
    # Loops until curr is None.
        if curr.value == value:
        # Checks if node’s value matches target.
            return True
            # Returns True if value found.
        curr = curr.next
        # Moves to next node.
    return False
    # Returns False if value not found.

# Prints: 1, 3, 4, 7.
traverse_list(head)
# Prints: 1 -> 3 -> 4 -> 7.
display(head)
# Prints: False (2 not in list).
print(search(head, 2))
# Prints: True (7 in list).
print(search(head, 7))

# Time and Space Complexity:
# - traverse_list: O(n) time (visits n nodes), O(1) space (only uses curr).
# - display: O(n) time (visits n nodes), O(n) space (stores n values in elements).
# - search: O(n) time (visits up to n nodes), O(1) space (only uses curr).




# –––––––––––––––––––––––––––––––––––––––––––––
# Background on join():

join()
# Syntax:
# separator.join(iterable)  # Returns a string; 'separator' is the string to join elements with
words = ["1", "2", "3", "4"]
result = " -> ".join(words)
print(result)
