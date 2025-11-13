# 121. Best Time to Buy and Sell Stock I
"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
 
Example 1:
    Input: prices = [7, 1, 5, 3, 6, 4]
    Output: 5

    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

https://www.youtube.com/watch?v=kJZrMGpyWpk

Solution: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
"""

def max_profit(prices):
    # Initialize variables
    min_price = float('inf')
    max_profit = 0

    # Iterate through the array
    for p in prices:
        if p < min_price:
            min_price = p
        
        profit = p - min_price
        if profit > max_profit:
            max_profit = profit
    
    return max_profit

prices = [7, 1, 5, 3, 6, 4]
print(max_profit(prices))
# Output: 5 → The best trade is buying at 1 and selling at 6 later, giving a maximum profit of 6 - 1 = 5.

"""
Time: O(N)
  - Let N = number of days (length of prices).
  - Loop through prices once → O(N).
      • Track the running minimum price in O(1).
      • Compute current profit and update max in O(1).
  - No nested loops — single sweep.
  - Overall: O(N).

Space: O(1)
  - Uses only two scalar variables: min_price and max_profit.
  - No extra data structures required.
  - Overall: O(1).

  
Interview Answer: Worst Case

Time: O(N)
  - Single pass updates min price and best profit.

Space: O(1)
  - Constant extra space for two variables.



  
---
Most IMPORTANT thing to Understand:
    • We're finding the **maximum difference** (sell - buy) where the buy happens before the sell.

    • Keep track of:
        - The lowest price seen so far (best buying point).
        - The highest profit achievable at each step.

    • We don't need to check all pairs — just keep updating min and max as we go.

---
Why this code Works:
    • Track running minimum price — simulates buying at the lowest price so far.

    • For each day, compute profit if sold today → price - min_price.

    • Update max_profit whenever a better profit appears.

    • Efficiency: one pass O(N), constant space O(1).

    • Intuition: Like walking through prices, remembering the cheapest buy day and updating your best profit as prices rise.

---
TLDR:
    • Scan once, track the lowest price and best profit difference — no need to compare all pairs.

---
Quick Example Walkthroughs:

Example 1: prices = [7, 1, 5, 3, 6, 4]
--------------------------------
min_price = inf, max_profit = 0

    Day 1: 7 → min=7 → profit=0 → max_profit=0  
    Day 2: 1 → min=1 → profit=0 → max_profit=0  
    Day 3: 5 → min=1 → profit=4 → max_profit=4  
    Day 4: 3 → min=1 → profit=2 → max_profit=4  
    Day 5: 6 → min=1 → profit=5 → max_profit=5  
    Day 6: 4 → min=1 → profit=3 → max_profit=5  

    Final Answer: 5 ✅ (Buy at 1, Sell at 6)


Example 2: prices = [7, 6, 4, 3, 1]
--------------------------------
min_price = inf, max_profit = 0

    Day 1: 7 → min=7 → profit=0 → max_profit=0  
    Day 2: 6 → min=6 → profit=0 → max_profit=0  
    Day 3: 4 → min=4 → profit=0 → max_profit=0  
    Day 4: 3 → min=3 → profit=0 → max_profit=0  
    Day 5: 1 → min=1 → profit=0 → max_profit=0  

    Final Answer: 0 ✅ (No profitable transaction)





---
Q: Why do we use `float('inf')` in this solution?
    • We need to track the **minimum price**, and starting at +∞ guarantees the first real price becomes the new minimum.

    • It avoids awkward edge cases like manually doing `min_price = prices[0]`.
        • Empty list → prices[0] crashes.

    • Makes the logic cleaner: every upcoming price is compared against an initial “impossibly large” value.

    • Ensures the algorithm works even if prices change later or input formats vary — the first number will always replace +∞.


"""



# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown 
def max_profit(prices):

    # Initialize variables
    min_price = float('inf')  # Track lowest price seen so far
    max_profit = 0            # Track highest profit possible

    # Iterate through the array
    for p in prices:          # Go through each day's price
        if p < min_price:     # If current price is lower
            min_price = p     # Update minimum price

        profit = p - min_price  # Calculate profit if sold today
        if profit > max_profit:  # If this is a new best profit
            max_profit = profit  # Update max profit

    # Return the maximum profit
    return max_profit         # Return highest profit (0 if none)




# ––––––––––––––––––––––––––––––––––––––––––––––
"""
GUIDE: float('inf') AND float('-inf')
----------------------------------------------

WHAT IS float('inf')?
    • Python's version of +∞ (positive infinity).
    • Larger than any real number.
    • Best starting value when you want to track the **minimum**.

WHAT IS float('-inf')?
    • Python;s version of -∞ (negative infinity).
    • Smaller than any real number.
    • Best starting value when you want to track the **maximum**.

WHY THIS MATTERS IN LEETCODE:
    • You often scan through a list and want to keep updating a “best so far.”
    • Using ±∞ ensures the very first element replaces your starting value.
    • Cleaner and safer than manually using the first element of the array.

MOST COMMON USE CASES (Beginner Level)
    1) Tracking a MIN value  ← MOST COMMON for float('inf')
         - Stock problems (best buy price)
         - Running minimum in number arrays

    2) Tracking a MAX value  ← MOST COMMON for float('-inf')
         - Max subarray variations
         - Running maximum in arrays

ANALOGY:
    • Tracking MIN: start with “infinite price” so the first real price is always better.
    • Tracking MAX: start with “lowest possible number” so the first real number is bigger.

CHEAT CODE:
    • Need MIN → float('inf')
    • Need MAX → float('-inf')
"""

# --------------------------------------------------------
# Example 1 (MOST COMMON): Track running minimum
# --------------------------------------------------------
def min_element(nums):
    m = float('inf')          # Start absurdly high
    for n in nums:
        if n < m:
            m = n
    return m

print(min_element([4, 2, 9, -1, 6]))  # → -1

# --------------------------------------------------------
# Example 2 (2nd most common): Track running maximum
# --------------------------------------------------------
def max_element(nums):
    m = float('-inf')         # Start absurdly low
    for n in nums:
        if n > m:
            m = n
    return m

print(max_element([4, 2, 9, -1, 6]))  # → 9

# --------------------------------------------------------
# Example 3 (very common beginner pattern): Stock problem
# --------------------------------------------------------
def max_profit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price

        profit = price - min_price

        if profit > max_profit:
            max_profit = profit

    return max_profit

print(max_profit([7, 1, 5, 3, 6, 4]))  # → 5










# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Brute Force
def maxProfit(self, prices):
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




# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Task: Find the maximum profit from buying and selling a stock once, given an array of daily prices.

# Return 0 if no profit is possible. Buy must occur before sell.

# Example: prices = [7, 1, 5, 3, 6, 4] → Output = 5 (buy at 1, sell at 6, profit = 6 - 1 = 5)

def max_profit(prices):  # Example: prices = [7, 1, 5, 3, 6, 4]

    # 1️⃣ Initialize variables
    # Set min_price to infinity to track the lowest price seen so far
    # Why? We need the minimum price to calculate the maximum possible profit
    min_price = float('inf')  # min_price = ∞

    # Initialize max_profit to 0 to track the highest profit achievable
    # Why? If no profit is possible (e.g., prices decrease), we return 0
    max_profit = 0  # max_profit = 0

    # 2️⃣ Iterate through the array
    # Loop through each price in the array
    # Why? We need to check each price as a potential buy or sell point
    for price in prices:  # price takes values [7, 1, 5, 3, 6, 4]
        # --- Iteration 1: price = 7 ---
        # Update min_price if the current price is lower
        # Why? A lower price could lead to a higher profit if sold later
        if price < min_price:  # price = 7, min_price = ∞, 7 < ∞ is true
            min_price = price  # min_price = 7
        # Calculate potential profit if selling at the current price
        # Why? We check the profit assuming we bought at the lowest price seen
        profit = price - min_price  # profit = 7 - 7 = 0
        # Update max_profit if the current profit is higher
        # Why? We want the largest possible profit
        if profit > max_profit:  # profit = 0, max_profit = 0, 0 > 0 is false, skip
            max_profit = profit
        # After Iteration 1: min_price = 7, max_profit = 0

        # --- Iteration 2: price = 1 ---
        if price == 1:
            if price < min_price:  # price = 1, min_price = 7, 1 < 7 is true
                min_price = price  # min_price = 1
            profit = price - min_price  # profit = 1 - 1 = 0
            if profit > max_profit:  # profit = 0, max_profit = 0, 0 > 0 is false, skip
                max_profit = profit
            # After Iteration 2: min_price = 1, max_profit = 0

        # --- Iteration 3: price = 5 ---
        if price == 5:
            if price < min_price:  # price = 5, min_price = 1, 5 < 1 is false, skip
                min_price = price
            profit = price - min_price  # profit = 5 - 1 = 4
            if profit > max_profit:  # profit = 4, max_profit = 0, 4 > 0 is true
                max_profit = profit  # max_profit = 4
            # After Iteration 3: min_price = 1, max_profit = 4

        # --- Iteration 4: price = 3 ---
        if price == 3:
            if price < min_price:  # price = 3, min_price = 1, 3 < 1 is false, skip
                min_price = price
            profit = price - min_price  # profit = 3 - 1 = 2
            if profit > max_profit:  # profit = 2, max_profit = 4, 2 > 4 is false, skip
                max_profit = profit
            # After Iteration 4: min_price = 1, max_profit = 4

        # --- Iteration 5: price = 6 ---
        if price == 6:
            if price < min_price:  # price = 6, min_price = 1, 6 < 1 is false, skip
                min_price = price
            profit = price - min_price  # profit = 6 - 1 = 5
            if profit > max_profit:  # profit = 5, max_profit = 4, 5 > 4 is true
                max_profit = profit  # max_profit = 5
            # After Iteration 5: min_price = 1, max_profit = 5

        # --- Iteration 6: price = 4 ---
        if price == 4:
            if price < min_price:  # price = 4, min_price = 1, 4 < 1 is false, skip
                min_price = price
            profit = price - min_price  # profit = 4 - 1 = 3
            if profit > max_profit:  # profit = 3, max_profit = 5, 3 > 5 is false, skip
                max_profit = profit
            # After Iteration 6: min_price = 1, max_profit = 5

    # 3️⃣ Return the maximum profit
    # Why? max_profit contains the largest profit achievable by buying and selling once
    return max_profit  # max_profit = 5


print(max_profit([7, 1, 5, 3, 6, 4]))  # Output: 5