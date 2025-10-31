# ----------------------------------------------------------
# ✅ WHAT TO MEMORIZE — CORE INTERVIEW MATERIAL
# ----------------------------------------------------------

# --------------------------------------------
# Singly Linked List
# --------------------------------------------
class SinglyNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# Insert AFTER a given node — O(1)
def add_node(prev_node, node_to_add):
    node_to_add.next = prev_node.next
    prev_node.next = node_to_add

# Delete the node AFTER a given node — O(1)
def delete_node(prev_node):
    prev_node.next = prev_node.next.next

# Forward Traversal — O(N)
def traverse_forward(head):
    curr = head
    while curr:
        print(curr.val, end=" → ")
        curr = curr.next
    print("None")

# Reverse in place — O(N) time / O(1) space
# Memorize mantra: save → reverse → move
def reverse_list(head):
    prev = None
    curr = head

    while curr:
        temp = curr.next      # save
        curr.next = prev      # reverse
        prev = curr           # move prev
        curr = temp           # move curr
    return prev

    # Note: True reverse traversal in a singly linked list requires recursion or reversing the list first — you can't go backward without extra structure.


# ---- Minimal SLL demo (single, clean pass) ----
# Build: 1 ⇄ 2 ⇄ 3
a = SinglyNode(1); b = SinglyNode(2); c = SinglyNode(3)
# Link them: a → b → c
a.next = b; b.next = c

# --------------------------------------------
# Insert 99 after 1:  1 → 99 → 2 → 3
x = SinglyNode(99)
# Insert x after a
add_node(a, x)

print("[SLL] after insert: "); traverse_forward(a)  
# Output: 1 → 99 → 2 → 3 → None

# --------------------------------------------
# Delete Example

# Delete node after 'a' (this removes node x (99))
delete_node(a)

print("Forward:")
traverse_forward(a)  # Output: 1 → 2 → 3 → None

# --------------------------------------------
# Forward traversal
print("Forward:")
traverse_forward(a)  # Output: 1 → 2 → 3 → None

# --------------------------------------------
# Reverse traversal
print("Reverse:")
result = reverse_list(a)
traverse_forward(result)  # Output: 3 → 2 → 1 → None





# --------------------------------------------
# Doubly linked list - UNDERSTAND (NO NEED TO MEMORIZE)
# --------------------------------------------
class DoublyNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

# Insert a Node
    # Insert new_node BEFORE node
    # node is a i. node_to_add is at i - 1
def add_node(node, node_to_add):
    prev_node = node.prev
    node_to_add.next = node
    node_to_add.prev = prev_node
    prev_node.next = node_to_add
    node.prev = node_to_add

# Delete a Node
    # node is at position i
def delete_node(node):
    prev_node = node.prev
    next_node = node.next
    prev_node.next = next_node
    next_node.prev = prev_node

# Forward traversal
def traverse_forward(head):
    curr = head
    while curr:
        print(curr.val, end=" ⇄ ")
        curr = curr.next
    print("None")

# Backward traversal
def traverse_backward(tail):
    curr = tail
    while curr:
        print(curr.val, end=" ⇄ ")
        curr = curr.prev
    print("None")


# Example setup: 1 ⇄ 2 ⇄ 3
a = DoublyNode(1); b = DoublyNode(2); c = DoublyNode(3)

# Link them together
a.next = b; b.prev = a; 
b.next = c; c.prev = b


# --------------------------------------------
# Insert Example

x = DoublyNode(99)
# # Insert a new node x (99) BEFORE node c (3)
add_node(c, x)

print("Forward:")
traverse_forward(a)  # Output: 1 ⇄ 2 ⇄ 99 ⇄ 3

print("Backward:")
traverse_backward(c)  # Output: 3 ⇄ 99 ⇄ 2 ⇄ 1


# --------------------------------------------
# Delete Example

# Delete node x (99)
delete_node(x)

print("Forward:")
traverse_forward(a)  # Output: 1 ⇄ 2 ⇄ 3

print("Backward:")
traverse_backward(c)  # Output: 3 ⇄ 2 ⇄ 1


# --------------------------------------------
# Forward traversal
print("Forward:")
traverse_forward(a)  # Output: 1 → 2 → 3 → None

# --------------------------------------------
# Reverse traversal
print("Reverse:")
traverse_backward(c)  # Output: 3 → 2 → 1 → None





# ----------------------------------------------------------
# EXTRAS — OPTIONAL / GOOD TO UNDERSTAND
# ----------------------------------------------------------
# Why keep: sometimes you just want a quick utility during practice.

# --------------------------------------------
# Singly Linked List Setup
# --------------------------------------------
class SinglyNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# Example: 1 ⇄ 2 ⇄ 3
a = SinglyNode(1); b = SinglyNode(2); c = SinglyNode(3)
# Link them: a → b → c
a.next = b; b.next = c


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Sum of values (simple traversal variant)
def get_sum(head):
    total = 0                    # Initialize sum to 0
    while head:                  # Traverse until end of list
        total += head.val        # Add current node's value to total
        head = head.next         # Move to next node
    return total                 # Return final sum

print("Sum:", get_sum(a))        # Output: 6

# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Get List Length
def get_length(head):
    n = 0                        # Initialize counter to 0
    while head:                  # Traverse until None
        n += 1                   # Increment counter for each node
        head = head.next         # Move to next node
    return n                     # Return total number of nodes

print("List length:", get_length(a))  # Output: 3

# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Check if Value Exists
def has_value(head, value):
    while head:                  # Traverse the list
        if head.val == value:    # Compare current node's value
            return True          # Return True if match found
        head = head.next         # Move to next node
    return False                 # Return False if not found

print("Has value 1:", has_value(a, 1))  # Output: True
print("Has value 5:", has_value(a, 5))  # Output: False