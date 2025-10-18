# 206. Reverse Linked List

# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Example 1:
    # Input: head = [1, 2, 3, 4, 5]
    # Output: [5, 4, 3, 2, 1]

# Example 2:
    # Input: head = [1, 2]
    # Output: [2, 1]

# Example 3:
    # Input: head = []
    # Output: []

# Solution: https://leetcode.com/problems/reverse-linked-list/description/


def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def reverseList(head):
    prev = None
    curr = head
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
        
    return prev













# """
# Add to notes if a hash table used what is the x and y values represent?
# """
