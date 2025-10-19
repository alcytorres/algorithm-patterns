# 92. Reverse Linked List II

# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

# Example 1
    # Input: head = [1, 2, 3, 4, 5], left = 2, right = 4
    # Output: [1, 4, 3, 2, 5]

# Example 2:
    # Input: head = [5], left = 1, right = 1
    # Output: [5]

# Solution: https://leetcode.com/problems/reverse-linked-list-ii/description/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next








# --------------------------------------------
# ✅ EXAMPLE 1: Linked list: head = [1 → 2 → 3 → 4 → 5]
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)

a.next = b; b.next = c; c.next = d; d.next = e

# Reverse and collect output
result = reverseList(a)
ans = []
curr = result
while curr:
    ans.append(curr.val)
    curr = curr.next
print("Output 1:", ans)   # [5, 4, 3, 2, 1]


# --------------------------------------------
# ✅ EXAMPLE 2: Linked list: head = [1 → 2]
a = ListNode(1)
b = ListNode(2)
a.next = b

result = reverseList(a)
ans = []
curr = result
while curr:
    ans.append(curr.val)
    curr = curr.next
print("Output 2:", ans)   # [2, 1]











"""
Add to notes if a hash table used what is the x and y values represent?
"""



