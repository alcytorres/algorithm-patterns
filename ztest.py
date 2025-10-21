










# # 92. Reverse Linked List II

# # Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

# # Example 1
#     # Input: head = [1, 2, 3, 4, 5], left = 2, right = 4
#     # Output: [1, 4, 3, 2, 5]

# # Example 2:
#     # Input: head = [5], left = 1, right = 1
#     # Output: [5]

# # Solution: https://leetcode.com/problems/reverse-linked-list-ii/description/


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# def reverseBetween(head, left, right):
#     if left == right: 
#         return head

#     dummy = ListNode(0, head)
#     prev = dummy

#     # 1) move prev to node BEFORE 'left'
#     for _ in range(left - 1):
#         prev = prev.next

#     # 2) reverse by repeatedly moving the node after 'curr' to the front
#     curr = prev.next
#     for _ in range(right - left):
#         nxt = curr.next           # node to relocate
#         curr.next = nxt.next      # detach nxt
#         nxt.next = prev.next      # put nxt at front of the sublist
#         prev.next = nxt           # reconnect front

#     return dummy.next


# # Helper to convert linked list to Python list for easy printing
# def to_list(head):
#     res = []
#     while head:
#         res.append(head.val)
#         head = head.next
#     return res


# # --------------------------------------------
# # ✅ EXAMPLE 1: head = [1, 2, 3, 4, 5], left = 2, right = 4
# a = ListNode(1)
# b = ListNode(2)
# c = ListNode(3)
# d = ListNode(4)
# e = ListNode(5)
# a.next = b; b.next = c; c.next = d; d.next = e

# result = reverseBetween(a, 2, 4)
# print("Output 1:", to_list(result))   # [1, 4, 3, 2, 5]


# # --------------------------------------------
# # ✅ EXAMPLE 2: head = [5], left = 1, right = 1
# a = ListNode(5)

# result = reverseBetween(a, 1, 1)
# print("Output 2:", to_list(result))   # [5]















# """
# Add to notes if a hash table used what is the x and y values represent?
# """



