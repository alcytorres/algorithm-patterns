# ----------------------------------------------------------
# ✅ WHAT TO MEMORIZE — CORE INTERVIEW MATERIAL
# ----------------------------------------------------------

# ============================================================
# Singly Linked List
# ============================================================
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
# INSERT 99 after 1
x = SinglyNode(99)
add_node(a, x)
print("SLL after insert:    ", end=""); traverse_forward(a)  
# Output: 1 → 99 → 2 → 3 → None

# --------------------------------------------
# DELETE node after 1 (removes 99)
delete_node(a)
print("SLL after delete:    ", end=""); traverse_forward(a)  
 # Output: 1 → 2 → 3 → None

# --------------------------------------------
# FORWARD traversal
print("SLL after traversal: ", end=""); traverse_forward(a)  
# Output: 1 → 2 → 3 → None

# --------------------------------------------
# REVERSE traversal
result = reverse_list(a)
print("SLL after reverse:   ", end=""); traverse_forward(result)
 # Output: 3 → 2 → 1 → None





# ============================================================
# Doubly Linked List — Understand the Mechanics (No Need to Memorize)
# ============================================================
class DoublyNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

# Insert a Node BEFORE another node — O(1)
def add_node(node, node_to_add):
    prev_node = node.prev
    node_to_add.next = node
    node_to_add.prev = prev_node
    prev_node.next = node_to_add
    node.prev = node_to_add

# Delete a Node — O(1)
def delete_node(node):
    prev_node = node.prev
    next_node = node.next
    prev_node.next = next_node
    next_node.prev = prev_node

# Forward Traversal — O(N)
def traverse_forward(head):
    curr = head
    while curr:
        print(curr.val, end=" ⇄ ")
        curr = curr.next
    print("None")

# Backward Traversal — O(N)
def traverse_backward(tail):
    curr = tail
    while curr:
        print(curr.val, end=" ⇄ ")
        curr = curr.prev
    print("None")


# ---- Minimal DLL demo (single, clean pass) ----
# Build: 1 ⇄ 2 ⇄ 3
a = DoublyNode(1); b = DoublyNode(2); c = DoublyNode(3)
a.next = b; b.prev = a; b.next = c; c.prev = b


# --------------------------------------------
# INSERT 99 before 3
x = DoublyNode(99)
add_node(c, x)
print("After insert (forward):  ", end=""); traverse_forward(a)
# Output: 1 ⇄ 2 ⇄ 99 ⇄ 3 ⇄ None

print("After insert (backward): ", end=""); traverse_backward(c)
# Output: 3 ⇄ 99 ⇄ 2 ⇄ 1 ⇄ None

# --------------------------------------------
# DELETE node 99
delete_node(x)
print("After delete (forward):  ", end=""); traverse_forward(a)
# Output: 1 ⇄ 2 ⇄ 3 ⇄ None

print("After delete (backward): ", end=""); traverse_backward(c)
# Output: 3 ⇄ 2 ⇄ 1 ⇄ None






# ============================================================
# EXTRAS — OPTIONAL / GOOD TO UNDERSTAND
# ============================================================
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

