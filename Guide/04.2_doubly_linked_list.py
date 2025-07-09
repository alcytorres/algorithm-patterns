# Big Picture:
# - Defines a doubly linked list where each node holds a value, a link to the next node, and a link to the previous node.
# - Creates a list: 3 <-> 1 <-> 7, starting from a single node (1).
# - Three functions: display shows the list as a string, insert_at_beginning adds a node at the start, insert_at_end adds a node at the end.
# - Doubly linked lists allow traversal forward (next) and backward (prev), unlike singly linked lists.

# curr = current node in traversal or operation.

class DoublyNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.value)

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



# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Class definition for a node in a doubly linked list
class DoublyNode:
    def __init__(self, value, next=None, prev=None):
        # Initializes node with value, next, and prev (default None).
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

# Display list as string: O(n)
# - Shows the list as a string (e.g., "3 <-> 1 <-> 7").
# - head: The first node of the list.
def display(head):
    # Checks if list is empty.
    if not head:
        return "Empty List"
        # Returns "Empty List" if no nodes.
    elements = []
    # Creates list to store values as strings.
    curr = head
    # Starts at head node.
    while curr:
        # Loops until curr is None (end of list).
        elements.append(str(curr.value))
        # Adds node’s value as string (e.g., "1").
        curr = curr.next
        # Moves to next node using next pointer.
    return " <-> ".join(elements)
    # Joins values with " <-> " (e.g., "3 <-> 1 <-> 7").


# Creates single node with value 1 (head and tail are same).
head = tail = DoublyNode(1) 
# Display initial list state
print("Initial list:", display(head))  # Output: 1


# - Empty list check: 
# `if not head:` evaluates to True if head is None (empty list), returning "Empty List" to handle the edge case safely.



# Insert at beginning: O(1)
# - Adds a new node with given value at the start of the list.
# - head: Current first node. tail: Current last node. value: Data for new node.
def insert_at_beginning(head, tail, value):
    new_node = DoublyNode(value)
    # Creates new node with value, next=None, prev=None.
    if not head:
        # Handles empty list case.
        return new_node, new_node
        # New node is both head and tail (single node).
    new_node.next = head
    # Links new node’s next to current head.
    head.prev = new_node
    # Links current head’s prev to new node.
    return new_node, tail
    # Returns new head (new node) and unchanged tail.

# Insert 3 at the beginning: 3 <-> 1
head, tail = insert_at_beginning(head, tail, 3)
print("After inserting 3 at beginning:", display(head))  # Output: 3 <-> 1


# - `return new_node, new_node`: 
    #  Tuple unpacks to head = new_node, tail = new_node, both set to node (e.g., value=5) for empty list.

# Baisc example: return a tuple
def get_pair(x, y):
    return x, y  # Returns a tuple (x, y)

result = get_pair(5, 5)
print(result)  # Outputs: (5, 5)
print(type(result))  # Outputs: <class 'tuple'>


# - Visualizing empty list insertion:
#   - Start: Empty list, head=None, tail=None.
#   - After insert_at_beginning(None, None, 5):
#     - New node: [value=5, next=None, prev=None].
#     - `return new_node, new_node`: Tuple tells caller to set head and tail to this node.
#     - After `head, tail = ...`: head and tail both point to [5].
#   - Why two values? Ensures head and tail are updated correctly for a single-node list.


# - Return syntax: 
    # `return new_node, tail` for non-empty list (new node is head, tail unchanged). Returns tuple to update head, tail.



# Insert at end: O(1)
# - Adds a new node with given value at the end of the list.
# - head: Current first node. tail: Current last node. value: Data for new node.
def insert_at_end(head, tail, value):
    new_node = DoublyNode(value)
    # Creates new node with value, next=None, prev=None.
    if not head:
        # Handles empty list case.
        return new_node, new_node
        # New node is both head and tail (single node).
    tail.next = new_node
    # Links current tail’s next to new node.
    new_node.prev = tail
    # Links new node’s prev to current tail.
    return head, new_node
    # Returns unchanged head and new tail (new node).

# Insert 7 at the end: 3 <-> 1 <-> 7
head, tail = insert_at_end(head, tail, 7)
print("After inserting 7 at end:", display(head))  # Output: 3 <-> 1 <-> 7



# Time and Space Complexity:
# - display: O(n) time (visits n nodes), O(n) space (stores n values in elements).
# - insert_at_beginning: O(1) time (updates pointers directly), O(1) space (one new node).
# - insert_at_end: O(1) time (updates pointers directly), O(1) space (one new node).


# Traversing the List
# - Forward traversal using next pointers:
curr = head
while curr is not None:
    print(curr.value)  # Prints 3, 1, 7
    curr = curr.next
# Walks forward through the list, printing each node’s value.

# - Backward traversal using prev pointers:
curr = tail
while curr is not None:
    print(curr.value)  # Prints 7, 1, 3
    curr = curr.prev
# Walks backward through the list, printing each node’s value.


# Clarifications for Learning:
# - Why head and tail? Doubly linked lists track both head (first node) and tail (last node) to enable O(1) insertions at either end.
# - Why return (head, tail)? Insertions may change head or tail, so functions return both to update the list’s references.
# - prev vs. next: next links to the following node, prev to the previous. Always update both when inserting to maintain list integrity.
# - Empty list case: When head is None, the list is empty. Inserting a node creates a single node that becomes both head and tail. If the list has nodes, insertions update only head (at beginning) or tail (at end).




# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Test the empty list case for insert_at_beginning

# Test empty list insertion: Call insert_at_beginning(None, None, value). Check head/tail values, next/prev (None), and head is tail (True).

class DoublyNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.value)

# Inserts a node at the beginning of a doubly linked list. O(1)
def insert_at_beginning(head, tail, value):
    new_node = DoublyNode(value)
    if not head:  # Empty list
        return new_node, new_node
    new_node.next = head
    head.prev = new_node
    return new_node, tail


# Start with empty list (head=None, tail=None)
head, tail = insert_at_beginning(None, None, 5)
    
# Verify the result
print("Head value:", head.value)  # Should print: 5
print("Tail value:", tail.value)  # Should print: 5
print("Head next:", head.next)    # Should print: None
print("Tail prev:", tail.prev)    # Should print: None
print("Head is tail:", head is tail)  # Should print: True (same node)


# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Test the empty list case for insert_at_end

# Test empty list insertion: Call insert_at_end(None, None, value). Check head/tail values, next/prev (None), and head is tail (True).

class DoublyNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.value)

# Inserts a node at the end of a doubly linked list. O(1)
def insert_at_end(head, tail, value):
    new_node = DoublyNode(value)
    if not head:  # Empty list
        return new_node, new_node
    tail.next = new_node
    new_node.prev = tail
    return head, new_node

# Start with empty list (head=None, tail=None)
head, tail = insert_at_end(None, None, 7)

# Verify the result
print("Head value:", head.value)  # Should print: 7
print("Tail value:", tail.value)  # Should print: 7
print("Head next:", head.next)    # Should print: None
print("Tail prev:", tail.prev)    # Should print: None
print("Head is tail:", head is tail)  # Should print: True (same node)


# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# - Visualize steps: Draw nodes as boxes (value inside). Label h (head), t (tail) above. Arrows → (n:next), ← (p:prev). Steps:
class DoublyNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.value)

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

# Creates single node with value 1 (head and tail are same).
head = tail = DoublyNode(1)
# Display initial list state
print("Initial list:", display(head))  # Output: 1


# Inserts a node at the beginning of a doubly linked list. O(1)
def insert_at_beginning(head, tail, value):
    new_node = DoublyNode(value)
    if not head:  # Empty list
        return new_node, new_node
    new_node.next = head
    head.prev = new_node
    return new_node, tail

# Insert 3 at the beginning: 3 <-> 1
head, tail = insert_at_beginning(head, tail, 3)
print("After inserting 3 at beginning:", display(head))  # Output: 3 <-> 1


# Inserts a node at the end of a doubly linked list. O(1)
def insert_at_end(head, tail, value):
    new_node = DoublyNode(value)
    if not head:  # Empty list
        return new_node, new_node
    tail.next = new_node
    new_node.prev = tail
    return head, new_node

# Insert 7 at the end: 3 <-> 1 <-> 7
head, tail = insert_at_end(head, tail, 7)
print("After inserting 7 at end:", display(head))  # Output: 3 <-> 1 <-> 7


# - Visualize steps: Draw nodes as boxes (value inside). Label h (head), t (tail) above. Arrows → (n:next), ← (p:prev). Steps:
#   1. `head = tail = DoublyNode(1)`: [p:None ← 1 → None:n], h,t on 1.
#   2. `insert_at_beginning(head, tail, 3)`:
#      a. `new_node = DoublyNode(3)`: [p:None ← 3 → None:n], 1 unchanged [p:None ← 1 → None:n], h,t on 1.
#      b. `new_node.next = head`: [p:None ← 3 → 1:n], 1 unchanged.
#      c. `head.prev = new_node`: [p:None ← 3 ↔ 1:n], [p:3 ← 1 → None:n].
#      d. `return new_node, tail`: [p:None ← 3 ↔ 1 → None:n], h on 3, t on 1.
#   3. `insert_at_end(head, tail, 7)`:
#      a. `new_node = DoublyNode(7)`: [p:None ← 7 → None:n], 3 ↔ 1 unchanged, h on 3, t on 1.
#      b. `tail.next = new_node`: [p:None ← 3 ↔ 1 → 7:n], [p:None ← 7 → None:n].
#      c. `new_node.prev = tail`: [p:None ← 3 ↔ 1 ↔ 7:n], [p:1 ← 7 → None:n].
#      d. `return head, new_node`: [p:None ← 3 ↔ 1 ↔ 7 → None:n], h on 3, t on 7.

