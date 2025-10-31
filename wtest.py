


class SinglyNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# Insert AFTER a given node — O(1)
def sll_insert_after(prev_node, node_to_add):
    node_to_add.next = prev_node.next
    prev_node.next = node_to_add

# Delete the node AFTER a given node — O(1)
def sll_delete_after(prev_node):
    if prev_node and prev_node.next:            # safety (prevents None errors)
        prev_node.next = prev_node.next.next

# Forward Traversal — O(N)
def sll_traverse_forward(head):
    curr = head
    while curr:
        print(curr.val, end=" → ")
        curr = curr.next
    print("None")

# Reverse in place — O(N) time / O(1) space
# Memorize mantra: save → reverse → move
def sll_reverse(head):
    prev = None
    curr = head
    while curr:
        temp = curr.next        # save
        curr.next = prev        # reverse
        prev = curr             # move prev
        curr = temp             # move curr
    return prev

# # ---- Minimal SLL demo (single, clean pass) ----
# # Build: 1 → 2 → 3
# a = SinglyNode(1); b = SinglyNode(2); c = SinglyNode(3)
# a.next = b; b.next = c

# # Insert 99 after 1: 1 → 99 → 2 → 3
# x = SinglyNode(99)
# sll_insert_after(a, x)
# print("[SLL] after insert:   ", end=""); sll_traverse_forward(a)

# # Delete node after 1: back to 1 → 2 → 3
# sll_delete_after(a)
# print("[SLL] after delete:   ", end=""); sll_traverse_forward(a)

# # Reverse: 3 → 2 → 1 → None
# rev = sll_reverse(a)
# print("[SLL] after reverse:  ", end=""); sll_traverse_forward(rev)











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

print("[SLL] after insert:    ", end=""); traverse_forward(a)  
# Output: 1 → 99 → 2 → 3 → None

# --------------------------------------------
# Delete node after 1: back to 1 → 2 → 3

# Delete node after 'a' (this removes node x (99))
delete_node(a)

print("[SLL] after delete:    ", end=""); traverse_forward(a)  
 # Output: 1 → 2 → 3 → None


# --------------------------------------------
# Forward traversal
print("[SLL] after traversal: ", end=""); traverse_forward(a)  
# Output: 1 → 2 → 3 → None

# --------------------------------------------
# Reverse traversal
result = reverse_list(a)
print("[SLL] after reverse:   ", end=""); sll_traverse_forward(result)
 # Output: 3 → 2 → 1 → None