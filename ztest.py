# Best time to buy a stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[i]

                if profit > 0:
                    max_profit = max(max_profit, profit)
        
        return max_profit
        # Time: O(N^2) (Brute Force)
        # Space: O(1)
        # This was modified from the video explanation to let max_profit = 0, this is better


def max_profit(prices):

    # 1️⃣ Initialize variables
    min_price = float('inf')
    max_profit = 0

    # 2️⃣ Iterate through the array
    for price in prices:
        if price < min_price:
            min_price = price
        
        profit = price - min_price

        if profit > max_profit:
            max_profit = profit

    # 3️⃣ Return the maximum profit
    return max_profit

print(max_profit([7, 1, 5, 3, 6, 4]))

# Time: O(n)
# Space: O(1)




# 141. Linked List Cycle
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head  # Start both pointers at the head of the list

        while fast and fast.next:  # Check if fast and its next node exist (avoid None errors)
            fast = fast.next.next  # Move fast pointer two steps ahead
            slow = slow.next       # Move slow pointer one step ahead

            if slow is fast:       # If slow and fast meet, a cycle exists
                return True        # Return True to indicate a cycle

        return False               # If we exit the loop, no cycle was found

# Time Complexity: O(n)
# Space Complexity: O(1)

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Test Case: Simple cycle
# List: 1 -> 2 -> 3 -> 2 (cycle back to node with value 2)
# Input: head = [1,2,3], pos = 1 (tail connects to index 1, node with value 2)
# Expected Output: True

# Create nodes
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

# Link nodes
node1.next = node2
node2.next = node3
node3.next = node2  # Create cycle: 3 points back to 2

# Test the solution
solution = Solution()
result = solution.hasCycle(node1)
print(result)  # Output: True







# 169. Majority Element - Brute Force
def majority_element_brute_force(nums):
    n = len(nums)  # Get length of array
    threshold = n // 2  # Majority requires > n/2 occurrences

    # Count occurrences of each number
    for num in nums:  # Check each number
        count = 0  # Reset count for current number
        for other in nums:  # Count how many times num appears
            if other == num:  # If numbers match
                count += 1  # Increment count
            if count > threshold:  # If count exceeds n/2
                return num  # Return majority element

    return -1  # Return -1 if no majority (though problem guarantees one)

    # Time: O(n²)
    # Space: O (1)


# 169. Majority Element - Solution 
def majority_element(nums):
    # 1️⃣ Set up variables to track candidate and its count
    answer = -1  # Holds the current majority element candidate
    count = 0    # Tracks the count difference for the candidate

    # 2️⃣ Loop through each number in the array
    for num in nums:
        if count == 0:         # If count is 0, pick a new candidate
            answer = num       # Set current number as new candidate
        
        # 3️⃣ Adjust count based on whether num matches candidate
        if answer == num:      # If current number is the candidate
            count += 1         # Increment count (strengthens candidate)
        else:                  # If current number is not the candidate
            count -= 1         # Decrement count (weakens candidate)

    # 4️⃣ Return the majority element (guaranteed to be correct)
    return answer          # Candidate with highest "net count" is majority

print(majority_element([2, 1, 2, 2, 2, 3]))  # Output: 2

# Time: O(n)
# Space: O (1)