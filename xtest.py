# # Singly Linked List: Insert & Delete a node
# class ListNode:
#     def __init__(self, val):
#         self.val = val
#         self.next = None

# # Let prev_node be the node at position i - 1
# def add_node(prev_node, node_to_add):
#     node_to_add.next = prev_node.next
#     prev_node.next = node_to_add

# # Delete the node right after prev_node
# def delete_node(prev_node):
#     prev_node.next = prev_node.next.next

# # Example: Insert 99 after 1 in list [1 → 2 → 3] → [1 → 99 → 2 → 3]
# a = ListNode(1)
# b = ListNode(2)
# c = ListNode(3)

# # Link them: a → b → c
# a.next = b
# b.next = c

# # Create a new node
# x = ListNode(99)

# # --------------------------------------------
# # Insert x after a (so list becomes: 1 → 99 → 2 → 3)
# add_node(a, x)

# # Print the full list to verify
# print("Forward:")
# curr = a
# while curr:
#     print(curr.val)
#     curr = curr.next
# # Output: 1  99  2  3

# # --------------------------------------------
# # Delete node after 'a' (this removes node 99)
# delete_node(a)

# # Print the list after deletion
# print("Forward:")
# curr = a
# while curr:
#     print(curr.val)
#     curr = curr.next
# # Output: 1  2  3










# Doubly linked list: Insert & Delete a node
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

# Let node be the node at position i
def add_node(node, node_to_add):
    prev_node = node.prev
    node_to_add.next = node
    node_to_add.prev = prev_node
    prev_node.next = node_to_add
    node.prev = node_to_add

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
