# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.

# Example
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].








def minStartValue(nums):
    # Start with startValue = 1. 
    start_value = 1

    # While we haven't found the first valid startValue
    while True:
        # The step-by-step total "total" equals startValue at the beginning.
        # Use boolean parameter "isValid" to record whether the total 
        # is larger than or equal to 1.
        total = start_value
        is_valid = True

        # Iterate over the array "nums".
        for num in nums:
            # In each iteration, calculate "total" 
            # plus the element "num" in the array.
            total += num

            # If "total" is less than 1, we shall try a larger startValue,
            # we mark "isValid" as "false" and break the current iteration.
            if total < 1:
                is_valid = False
                break

        # If "isVaild" is true, meaning "total" is never less than 1 in the
        # iteration, therefore we return this "startValue". Otherwise, we 
        # go ahead and try "startValue" + 1 as the new "startValue". 
        if is_valid:
            return start_value
        else:
            start_value += 1






# Alternative solution 
def minStartValue(nums):
    # We use "total" for current step-by-step total, "min_val" for minimum 
    # step-by-step total among all sums. Since we always start with 
    # startValue = 0, therefore the initial current step-by-step total is 0, 
    # thus we set "total" and "min_val" be 0. 
    min_val = 0
    total = 0

    # Iterate over the array and get the minimum step-by-step total.
    for num in nums:
        total += num
        min_val = min(min_val, total)

    # We have to change the minimum step-by-step total to 1, 
    # by increasing the startValue from 0 to -min_val + 1, 
    # which is just the minimum startValue we want.
    return -min_val + 1
