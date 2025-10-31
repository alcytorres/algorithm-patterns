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

# Insert a Node
    # prev_node is the node at position i - 1
def add_node(prev_node, node_to_add):
    node_to_add.next = prev_node.next
    prev_node.next = node_to_add

# Delete a Node
    # Delete the node right after prev_node
def delete_node(prev_node):
    prev_node.next = prev_node.next.next

# Forward Traversal Pattern
def traverse_forward(head):
    curr = head
    while curr:
        print(curr.val, end=" → ")
        curr = curr.next
    print("None")

# Reversal Pattern (memorize “save → reverse → move”)
def reverse_list(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

    # Note: True reverse traversal in a singly linked list requires recursion or reversing the list first — you can't go backward without extra structure.


# --------------------------------------------
# Example setup: 1 ⇄ 2 ⇄ 3
a = SinglyNode(1); b = SinglyNode(2); c = SinglyNode(3)
# Link them: a → b → c
a.next = b; b.next = c

# --------------------------------------------
# Insert Example

x = SinglyNode(99)
# Insert x after a
add_node(a, x)

print("Forward:")
traverse_forward(a)  # Output: 1 → 99 → 2 → 3 → None

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
# Doubly linked list
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





# --------------------------------------------
# Doubly Linked List with Sentinels
# --------------------------------------------
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

def add_to_end(node_to_add):
    node_to_add.next = tail
    node_to_add.prev = tail.prev
    tail.prev.next = node_to_add
    tail.prev = node_to_add

def remove_from_end():
    if head.next == tail:
        return

    node_to_remove = tail.prev
    node_to_remove.prev.next = tail
    tail.prev = node_to_remove.prev

def add_to_start(node_to_add):
    node_to_add.prev = head
    node_to_add.next = head.next
    head.next.prev = node_to_add
    head.next = node_to_add

def remove_from_start():
    if head.next == tail:
        return
    
    node_to_remove = head.next
    node_to_remove.next.prev = head
    head.next = node_to_remove.next

# Build empty DLL with sentinels
head = ListNode(None)
tail = ListNode(None)
head.next = tail
tail.prev = head


# Example setup: 1 ⇄ 2 ⇄ 3
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)

# Link them together
head.next = a
a.prev = head
a.next = b
b.prev = a
b.next = c
c.prev = b
c.next = tail
tail.prev = c


# --------------------------------------------
# INITIAL LIST TRAVERSAL 
print("\nForward:")
curr = head.next
while curr is not tail:
    print(curr.val)
    curr = curr.next
# Output: 1 ⇄ 2 ⇄ 3

# --------------------------------------------
# INSERTING AT THE TAIL (ADD NODE TO END)
y = ListNode(77)
add_to_end(y)
# List: 1 ⇄ 2 ⇄ 3 ⇄ 77

# --------------------------------------------
# 🗑️ DELETING THE TAIL (REMOVE LAST NODE)
if tail.prev is not head:
    remove_from_end()
# List now: 1 ⇄ 2 ⇄ 3

# # --------------------------------------------
# INSERTING AT THE HEAD (ADD NODE TO START)
x = ListNode(99)
add_to_start(x)
# List: 99 ⇄ 1 ⇄ 2 ⇄ 3

# --------------------------------------------
# 🗑️ DELETING THE HEAD (REMOVE FIRST NODE)
if head.next is not tail:
    remove_from_start()
# List now: 1 ⇄ 2 ⇄ 3

# --------------------------------------------
# 🔁 FINAL LIST TRAVERSAL (PRINT RESULT)
print("Forward:")
curr = head.next
while curr is not tail:
    print(curr.val)
    curr = curr.next
# Expected:
# 1
# 2
# 3









# --------------------------------------------
# Doubly linked list: 
# --------------------------------------------
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
print("After inserting 3 at beginning:", display(head))  
# Output: 3 <-> 1

# Insert 7 at the end: 3 <-> 1 <-> 7
head, tail = insert_at_end(head, tail, 7)
print("After inserting 7 at end:", display(head))  
# Output: 3 <-> 1 <-> 7





# ----------------------------------------------------------
# EXTRAS — OPTIONAL / GOOD TO UNDERSTAND
# ----------------------------------------------------------

# Sum of values (simple traversal variant)
def get_sum(head):
    count = 0
    while head:
        count += head.val
        head = head.next  # move forward one node
    return count

# Print total sum
print(get_sum(a))
# Output: 6


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# # Get List Length
def get_length(head):
    count = 0          # Initialize counter
    curr = head        # Start at head
    while curr:        # Traverse until None
        count += 1     # Increment for each node
        curr = curr.next  # Move to next node
    return count       # Return total nodes

# Test get_length
print("List length:", get_length(head))  # Output: 3 (for 3 <-> 1 <-> 7)


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Check if Value Exists
def has_value(head, value):
    curr = head
    while curr:
        if curr.value == value:
            return True
        curr = curr.next
    return False

# Test has_value
print("Has value 1:", has_value(head, 1))  # Output: True
print("Has value 5:", has_value(head, 5))  # Output: False