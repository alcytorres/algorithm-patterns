







# # """
# # Add to notes if a hash table used what is the x and y values represent?
# # """









"""
ALCY — LINKED LISTS STUDY GUIDE (Tight, interview-ready)

What I changed & why (high-impact only):
- Renamed overlapping function names (SLL vs DLL) to avoid collisions in one file.
- Added light safety checks to O(1) delete to prevent None errors.
- Removed duplicate prints / repeated demos that added noise.
- Kept DLL as “understand only,” minimal demo; trimmed commentary.
- Moved “optional utilities” to the end and commented out their demo calls to avoid state confusion.

Stick to this and your separate write-ups for the 8 problems you listed.
"""

# ----------------------------------------------------------
# ✅ WHAT TO MEMORIZE — CORE INTERVIEW MATERIAL (SINGLY LL)
# ----------------------------------------------------------

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

# ---- Minimal SLL demo (single, clean pass) ----
# Build: 1 → 2 → 3
a = SinglyNode(1); b = SinglyNode(2); c = SinglyNode(3)
a.next = b; b.next = c

# Insert 99 after 1: 1 → 99 → 2 → 3
x = SinglyNode(99)
sll_insert_after(a, x)
print("[SLL] after insert:   ", end=""); sll_traverse_forward(a)

# Delete node after 1: back to 1 → 2 → 3
sll_delete_after(a)
print("[SLL] after delete:   ", end=""); sll_traverse_forward(a)

# Reverse: 3 → 2 → 1 → None
rev = sll_reverse(a)
print("[SLL] after reverse:  ", end=""); sll_traverse_forward(rev)


# ----------------------------------------------------------
# 📘 DOUBLY LINKED LIST — UNDERSTAND (NO NEED TO MEMORIZE)
# ----------------------------------------------------------

class DoublyNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

# Insert new_node BEFORE `node` — O(1)
def dll_insert_before(node, node_to_add):
    prev_node = node.prev
    node_to_add.next = node
    node_to_add.prev = prev_node
    if prev_node: prev_node.next = node_to_add
    node.prev = node_to_add

# Delete `node` — O(1)
def dll_delete(node):
    prev_node, next_node = node.prev, node.next
    if prev_node: prev_node.next = next_node
    if next_node: next_node.prev = prev_node

def dll_traverse_forward(head):
    curr = head
    while curr:
        print(curr.val, end=" ⇄ ")
        curr = curr.next
    print("None")

def dll_traverse_backward(tail):
    curr = tail
    while curr:
        print(curr.val, end=" ⇄ ")
        curr = curr.prev
    print("None")

# ---- Tiny DLL demo (keep minimal) ----
d1 = DoublyNode(1); d2 = DoublyNode(2); d3 = DoublyNode(3)
d1.next = d2; d2.prev = d1; d2.next = d3; d3.prev = d2

dll_insert_before(d3, DoublyNode(99))    # 1 ⇄ 2 ⇄ 99 ⇄ 3
print("[DLL] forward (ins):  ", end=""); dll_traverse_forward(d1)
print("[DLL] backward (ins): ", end=""); dll_traverse_backward(d3)

dll_delete(d2)                           # 1 ⇄ 99 ⇄ 3
print("[DLL] forward (del):  ", end=""); dll_traverse_forward(d1)
print("[DLL] backward (del): ", end=""); dll_traverse_backward(d3)


# ----------------------------------------------------------
# EXTRAS — OPTIONAL / GOOD TO UNDERSTAND (SINGLY ONLY)
# (Utilities kept; demo calls commented to avoid state conflicts)
# ----------------------------------------------------------

def sll_sum(head):        # O(N)
    total = 0
    while head:
        total += head.val
        head = head.next
    return total

def sll_length(head):     # O(N)
    n = 0
    while head:
        n += 1
        head = head.next
    return n

def sll_has_value(head, value):  # O(N)
    while head:
        if head.val == value:
            return True
        head = head.next
    return False

# # Optional quick checks (commented out by default)
# fresh = SinglyNode(3); fresh.next = SinglyNode(1); fresh.next.next = SinglyNode(7)
# print("sum:", sll_sum(fresh))                 # 11
# print("len:", sll_length(fresh))              # 3
# print("has 1:", sll_has_value(fresh, 1))      # True
# print("has 5:", sll_has_value(fresh, 5))      # False


