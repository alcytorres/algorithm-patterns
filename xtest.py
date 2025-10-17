# --------------------------------------------
# Singly Linked List
# --------------------------------------------

class SinglyNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# Inserting a Node
# Let prev_node be the node at position i - 1
def add_node(prev_node, node_to_add):
    node_to_add.next = prev_node.next
    prev_node.next = node_to_add

# Deleting a Node
# Delete the node right after prev_node
def delete_node(prev_node):
    prev_node.next = prev_node.next.next

# Traversal (Iterating)
def get_sum(head):
    ans = 0
    while head:
        ans += head.val
        head = head.next  # move forward one node
    return ans

# Example setup: 1 ⇄ 2 ⇄ 3
a = SinglyNode(1)
b = SinglyNode(2)
c = SinglyNode(3)

# Link them: a → b → c
a.next = b
b.next = c

# Mark the start of the list
head = a

# Create a new node
x = SinglyNode(99)

# --------------------------------------------
# Insert x after a (so list becomes: 1 → 99 → 2 → 3)
add_node(a, x)

# Print the full list to verify
print("Forward:")
curr = a
while curr:
    print(curr.val)
    curr = curr.next
# Output: 1  99  2  3

# --------------------------------------------
# Delete node after 'a' (this removes node 99)
delete_node(a)

# Print the list after deletion
print("Forward:")
curr = a
while curr:
    print(curr.val)
    curr = curr.next
# Output: 1  2  3






# --------------------------------------------
# Doubly linked list
# --------------------------------------------
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

# Insert new_node BEFORE node
    # Let node be the node at position i
def add_node(node, node_to_add):
    prev_node = node.prev
    node_to_add.next = node
    node_to_add.prev = prev_node
    prev_node.next = node_to_add
    node.prev = node_to_add

# Delete node
    # Let node be the node at position i
def delete_node(node):
    prev_node = node.prev
    next_node = node.next
    prev_node.next = next_node
    next_node.prev = prev_node


# Example setup: 1 ⇄ 2 ⇄ 3
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)

# Link them together
a.next = b
b.prev = a
b.next = c
c.prev = b

# --------------------------------------------
# ✅ Insert a new node (99) BEFORE node c
x = ListNode(99)
add_node(c, x)
# List becomes: 1 ⇄ 2 ⇄ 99 ⇄ 3

# Print the list forward
print("Forward:")
curr = a
while curr:
    print(curr.val)
    curr = curr.next


# --------------------------------------------
# ✅ Delete node b (value = 2)
delete_node(b)
# List becomes: 1 ⇄ 99 ⇄ 3

# Print the list forward
print("\nForward:")
curr = a
while curr:
    print(curr.val)
    curr = curr.next  # 1 ⇄ 99 ⇄ 3

# Print the list backward
print("Backward:")
curr = c
while curr:
    print(curr.val)
    curr = curr.prev  # 3 ⇄ 99 ⇄ 1








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
# ✅ INSERTING AT THE TAIL (ADD NODE TO END)
y = ListNode(77)
add_to_end(y)
# List: 1 ⇄ 2 ⇄ 3 ⇄ 77

# --------------------------------------------
# 🗑️ DELETING THE TAIL (REMOVE LAST NODE)
if tail.prev is not head:
    remove_from_end()
# List now: 1 ⇄ 2 ⇄ 3

# # --------------------------------------------
# ✅ INSERTING AT THE HEAD (ADD NODE TO START)
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
