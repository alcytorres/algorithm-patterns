class ListNode:
    def __init__(self, val):
        self.val = val      # store this node’s value
        self.next = None    # start unlinked; will later point to next node

# Build nodes
one = ListNode(1)
two = ListNode(2)
three = ListNode(3)

# Link them together
one.next = two
two.next = three

# Mark the start of the list
head = one

# print(head.val)            # 1
# print(head.next.val)       # 2
# print(head.next.next.val)  # 3


def longestOnes(nums, k):
    left = ans = curr = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            curr += 1
        
        while curr > k:
            if nums[left] == 0:
                curr -= 1
            left += 1
        
        ans = max(ans, right - left + 1)
    
    return ans

nums = [1, 0, 0, 1, 1, 0, 1]
k = 2
print(longestOnes(nums, k))
# Output: 5




def longestOnes(nums, k):
    l = ans = curr = 0

    for r in range(len(nums)):
        if nums[r] == 0:
            curr += 1
        
        while curr > k:
            if nums[l] == 0:
                curr -= 1
            l += 1
        
        ans = max(ans, r - l + 1)
    
    return ans

nums = [1, 0, 0, 1, 1, 0, 1]
k = 2
print(longestOnes(nums, k))
# Output: 5
