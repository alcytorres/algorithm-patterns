# Breakdown this code
# Explain each line and the syntax
# Explain big picture what is happening 
# Basic exrecise for this 


# –––––––––––––––––––––––––––––––––––––––––––––
# Background on iter() and next():

# Create a list and get its iterator
nums = [1, 2, 3]
iterator = iter(nums)

# Use next() to get items one by one
print(next(iterator))  # Outputs: 1
print(next(iterator))  # Outputs: 2
print(next(iterator))  # Outputs: 3
print(next(iterator))  # Raises StopIteration (no more items)
print(next(iterator, "end"))  # Outputs: end

# Check the iterator type
print(type(iterator))  # Output: <class 'list_iterator'>


# Create an iterator from a string
text = "abc"
iterator = iter(text)

# Use next() with a default value to avoid StopIteration
print(next(iterator, "end"))  # Outputs: a
print(next(iterator, "end"))  # Outputs: b
print(next(iterator, "end"))  # Outputs: c
print(next(iterator, "end"))  # Outputs: end (default when iterator is exhausted)

# Check the iterator type
print(type(iterator))  # Output: <class 'str_iterator'>


join()
# Syntax:
# separator.join(iterable)  # Returns a string; 'separator' is the string to join elements with
words = ["1", "2", "3", "4"]
result = " -> ".join(words)
print(result)


# Big Picture:
# - This code defines a singly linked list, where each node holds a value and a link to the next node.
# - It creates a list: 1 -> 3 -> 4 -> 7 -> None.
# - Three functions: traverse_list prints each node’s value, display shows the list as a string, and search checks if a value exists.
# - Each function iterates through the list, making them O(n) in time complexity.


# The next in SinglyNode is unrelated to the next() iterator function; it’s just a naming coincidence. 
# It refers to the next node in the linked list, not iteration.


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
current = head
while current is not None:
    print(current.value)  # Prints 1, 3, 4, 7
    current = current.next
# It’s like walking through the chain, printing each node’s value until the end.


# Traverse and print: O(n)
# - Defines a function to print each node’s value in the list.
# - head: The starting node of the list (e.g., head with value 1).
def traverse_list(head):
# Prints each node’s value. O(n) time.
    curr = head
    # Starts at head node.
    while curr:
    # Loops until curr is None.
        print(curr)
        # Prints node’s value (e.g., 1, 3, 4, 7).
        curr = curr.next
        # Moves to next node.

# Display list as string (e.g., "1 -> 3 -> 4 -> 7"): O(n)
# - Defines a function to show the list as a string (e.g., "1 -> 3 -> 4 -> 7").
# - head: The starting node of the list.
def display(head):
# Shows list as string (e.g., "1 -> 3 -> 4 -> 7"). O(n) time.
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
    print(" -> ".join(elements))
    # Prints values joined by " -> ".

# Search for value: O(n)
# - Defines a function to check if a value exists in the list.
# - head: The starting node.
# - value: The value to find (e.g., 2 or 7).
def search(head, value):
# Checks if value exists in list. O(n) time.
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
