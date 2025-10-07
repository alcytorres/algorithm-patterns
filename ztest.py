








class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    
    def get_sum(head):
        if not head:
            return 0
        
        return head.val + ListNode.get_sum(head.next)

one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
one.next = two
two.next = three
head = one
# print(head.val)
# print(head.next.val)
# print(head.next.next.val)

result = ListNode.get_sum(head)
# print(result)  # Output: 6
# print(head)





class Human:
    def __init__(self, age):
        self.age = age
    
    def __str__(self):
        return f"A human who has an age of {self.age}."

    def older_younger_than(self, other_age):
        if self.age > other_age:
            print("our age is bigger than their age.")
        elif self.age == other_age:
            print("our age is equal to their age.")
        else:
            print("our age is less than their age.")

# h1 = Human(10)
# h2 = Human(20)
# h3 = Human(30)
# h1.next = h2
# print(h1)
# print(h1.next)


# print(h1.age)














"""
Add to notes if a hash table used what is the x and y values represent?
"""

# print(3%2)
# print(11//2)









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


