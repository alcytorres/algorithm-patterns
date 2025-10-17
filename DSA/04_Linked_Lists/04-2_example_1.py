# Find the Middle Node in a Singly Linked List

# Example 1: Given the head of a linked list with an odd number of nodes head, return the value of the node in the middle.

# For example, given a linked list that represents 1 -> 2 -> 3 -> 4 -> 5, return 3.

# --------------------------------------------
# FIND MIDDLE NODE OF A LINKED LIST
# --------------------------------------------
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def get_middle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow.val

# --------------------------------------------
# ✅ EXAMPLE Linked list: 1 → 2 → 3 → 4 → 5
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)

# Link them together
a.next = b
b.next = c
c.next = d
d.next = e

# Print Result
print(get_middle(a))
# Output: 3





# --------------------------------------------
# Alternative less good Solution
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def get_middle(head):
    length = 0
    dummy = head
    while dummy:
        length += 1
        dummy = dummy.next
    
    for _ in range(length // 2):
        head = head.next
    
    return head.val

# --------------------------------------------
# ✅ EXAMPLE Linked list: 1 → 2 → 3 → 4 → 5
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)

# Link them together
a.next = b
b.next = c
c.next = d
d.next = e

# Print Result
print(get_middle(a))
# Output: 3



# --------------------------------------------
# Brute Force
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def get_middle(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr[len(arr) // 2]

# --------------------------------------------
# ✅ EXAMPLE Linked list: 1 → 2 → 3 → 4 → 5
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)

# Link them together
a.next = b
b.next = c
c.next = d
d.next = e

# Print Result
print(get_middle(a))
# Output: 3