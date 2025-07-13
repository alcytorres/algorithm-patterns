nums = [1, 4, 8, 3]

max_num = nums[0]
for num in nums:
    if num > max_num:
        max_num = num

print(max_num)

def find_max(num):
    max_num = nums[0]
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num

nums = [1, 4, 8, 3]
print(find_max(nums))