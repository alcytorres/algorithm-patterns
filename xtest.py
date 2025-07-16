

def sortedSquares(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    
    left = 0
    right = len(nums) - 1
    ans = []

    while left < right:
        if abs(nums[left]) < abs(nums[right]):
            ans.append(nums[left])
            left += 1
        else:
            ans.append(nums[right])
            right -= 1
    
    return ans

print(sortedSquares([-10,-5,1,2,4,7]))

# print(sortedSquares([-4,-1,0,3,10]))










# n = 6
# result = [0,0,0,0,0,0]
# left = 0,
# right = 5

# i=5 start=5, stop at 0, step=-1
# square = -10
# result = [0,0,0,0,0,100]
# left = 1

# i=4 start=4. stop at 0, step=-1
# square = 7
# right = 4
# result = [0,0,0,0,49,100]

# i=3
# square = 5
# left = 2
# result = [0,0,0,25,49,100]

# i=2
# square = 4
# right = 3
# result = [0,0,16,25,49,100]

# i=1
# square = 2
# right = 2
# result = [0,4,16,25,49,100]

# i=1
# square = 1
# = 1
# result = [1,4,16,25,49,100]