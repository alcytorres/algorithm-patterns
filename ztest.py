# Singly Node
class SinglyNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    
    # Traversal (Iterating)
    def get_sum(head):
        ans = 0
        while head:
            ans += head.val
            head = head.next  # move forward one node
        return ans
    
    # Inserting a Node
    # Let prev_node be the node at position i - 1
    def add_node(prev_node, node_to_add):
        node_to_add.next = prev_node.next
        prev_node.next = node_to_add

    # Deleting a Node
    # Delete the node right after prev_node
    def delete_node(prev_node):
        prev_node.next = prev_node.next.next



# Build nodes
a = SinglyNode(1)
b = SinglyNode(2)
c = SinglyNode(3)

# Link them together a → b → c
a.next = b
b.next = c

# Mark the start of the list
head = a



# Create a new node
x = SinglyNode(99)
SinglyNode.add_node(head, x)

# Print the full list to verify
curr = head
while curr:
    print(curr.val)
    curr = curr.next
# Output: 1  99  2  3




# Doubly Node




"""
Simple Breakdown:
    prev_node = node.prev          = 2
    node_to_add.next = node        = 3
    node_to_add.prev = prev_node   = 2
    prev_node.next = node_to_add   = 99
    node.prev = node_to_add        = 99

"""


























# """
# Add to notes if a hash table used what is the x and y values represent?
# """







# def fn(nums):
#     ans = {}
#     for i, num in enumerate(nums):
#         ans[i] = num
#     return ans
    
# nums = ['a', 'b', 'c']
# print(fn(nums))


# nums = ['a', 'b', 'c']
# for i, num in enumerate(nums):
#     print(i, num)  
# # Prints: 
# # 0 a
# # 1 b
# # 2 c


