class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def middleNode(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

# --------------------------------------------
# ✅ EXAMPLE 1: Linked list: 1 → 2 → 3 → 4 → 5
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b; b.next = c; c.next = d; d.next = e

result = middleNode(a)
curr = result
output1 = []
while curr:
    output1.append(curr.val)
    curr = curr.next
print("Output 1:", output1)   # [3, 4, 5]


# --------------------------------------------
# ✅ EXAMPLE 2: Linked list: 1 → 2 → 3 → 4 → 5 → 6
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(6)
a.next = b; b.next = c; c.next = d; d.next = e; e.next = f

result = middleNode(a)
curr = result
output2 = []
while curr:
    output2.append(curr.val)
    curr = curr.next
print("Output 2:", output2)   # [4, 5, 6]









# """
# Add to notes if a hash table used what is the x and y values represent?
# """


