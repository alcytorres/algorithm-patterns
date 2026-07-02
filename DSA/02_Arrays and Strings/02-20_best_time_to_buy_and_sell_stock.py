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

# Single Pass: Track Min Price + Max Profit

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

        profit = p - min_price   # Calculate profit if sold today
        if profit > max_profit:  # If this is a new best profit
            max_profit = profit  # Update max profit

    # Return the maximum profit
    return max_profit         # Return highest profit (0 if none)


"""
Time: O(N)
  - Let N = number of days (length of prices).
  - One loop through prices → O(N).
      • Update running minimum price → O(1).
      • Compute current profit and update max profit → O(1).
  - No nested loops — each price is visited once.
  - Overall: O(N).

Space: O(1)
  - Uses only two scalar variables: min_price and max_profit.
  - No extra data structures required.
  - Overall: O(1).

  
Interview Answer: Worst Case

Time: O(N)
  - Single pass through prices; each day updates min price and best profit in O(1).

Space: O(1)
  - Constant extra space for two variables.


  

---
Most IMPORTANT thing to Understand:
    • We want the biggest profit from one buy-then-sell trade, where buy happens before sell.

    • At each day, the best buy price is the lowest price seen so far — not every past day.

    • `min_price` tracks that cheapest buy so far.

    • `max_profit` tracks the best profit if we sold on any day up to now.

    • We never need to compare every buy/sell pair — one pass is enough.

---
Why this code Works:
    • Running minimum:
        • `min_price` stores the lowest price seen before the current day.
        • When a new lower price appears, it becomes the new best buy point.

    • Profit at each day:
        • `profit = p - min_price` means "if I bought at the cheapest day so far and sold today, what do I make?"
        • If that profit beats `max_profit`, we save it.

    • Efficiency:
        • Brute force checks all pairs → O(N²).
        • This scans once → O(N) time, O(1) space.

    • Intuition:
        • Walk through prices left to right.
        • Remember the cheapest day to buy.
        • Every time price goes up, ask: "Is this my best sell day so far?"

---
TLDR:
    • One pass tracks the lowest buy price seen so far and the best profit if you sell today — no need to check all pairs.


---
Quick Example 1 Walkthrough:
    prices = [7, 1, 5, 3, 6, 4]

    Step 1: Start with min_price = ∞, max_profit = 0

    Step 2: Walk through each price
        • Day 1 (7): min becomes 7, profit = 0, max stays 0
        • Day 2 (1): min becomes 1, profit = 0, max stays 0
        • Day 3 (5): min stays 1, profit = 4, max becomes 4
        • Day 4 (3): min stays 1, profit = 2, max stays 4
        • Day 5 (6): min stays 1, profit = 5, max becomes 5
        • Day 6 (4): min stays 1, profit = 3, max stays 5

    Final Answer: 5 (buy at 1, sell at 6)


---
Quick Example 2 Walkthrough:
    prices = [7, 6, 4, 3, 1]

    Step 1: Start with min_price = ∞, max_profit = 0

    Step 2: Walk through each price
        • Day 1 (7): min becomes 7, profit = 0, max stays 0
        • Day 2 (6): min becomes 6, profit = 0, max stays 0
        • Day 3 (4): min becomes 4, profit = 0, max stays 0
        • Day 4 (3): min becomes 3, profit = 0, max stays 0
        • Day 5 (1): min becomes 1, profit = 0, max stays 0

    Final Answer: 0 (no profitable transaction — prices only go down)



---
Full Example 1 Walkthrough:
    prices = [7, 1, 5, 3, 6, 4]

    Starting State:
        min_price = inf
        max_profit = 0

        About to process first price: p = 7

    Loop Iteration 1:
        Current price:
            p = 7

        Check minimum:
            Is 7 < inf? → YES
            min_price = 7

        Calculate profit:
            profit = 7 - 7 = 0

        Check max profit:
            Is 0 > 0? → NO
            max_profit stays 0

        Now:
            min_price = 7
            max_profit = 0

    --------------------------------------------------

    Loop Iteration 2:
        Current price:
            p = 1

        Check minimum:
            Is 1 < 7? → YES
            min_price = 1

        Calculate profit:
            profit = 1 - 1 = 0

        Check max profit:
            Is 0 > 0? → NO
            max_profit stays 0

        Now:
            min_price = 1
            max_profit = 0

    --------------------------------------------------

    Loop Iteration 3:
        Current price:
            p = 5

        Check minimum:
            Is 5 < 1? → NO
            min_price stays 1

        Calculate profit:
            profit = 5 - 1 = 4

        Check max profit:
            Is 4 > 0? → YES
            max_profit = 4

        Now:
            min_price = 1
            max_profit = 4

    --------------------------------------------------

    Loop Iteration 4:
        Current price:
            p = 3

        Check minimum:
            Is 3 < 1? → NO
            min_price stays 1

        Calculate profit:
            profit = 3 - 1 = 2

        Check max profit:
            Is 2 > 4? → NO
            max_profit stays 4

        Now:
            min_price = 1
            max_profit = 4

    --------------------------------------------------

    Loop Iteration 5:
        Current price:
            p = 6

        Check minimum:
            Is 6 < 1? → NO
            min_price stays 1

        Calculate profit:
            profit = 6 - 1 = 5

        Check max profit:
            Is 5 > 4? → YES
            max_profit = 5

        Now:
            min_price = 1
            max_profit = 5

    --------------------------------------------------

    Loop Iteration 6:
        Current price:
            p = 4

        Check minimum:
            Is 4 < 1? → NO
            min_price stays 1

        Calculate profit:
            profit = 4 - 1 = 3

        Check max profit:
            Is 3 > 5? → NO
            max_profit stays 5

        Now:
            min_price = 1
            max_profit = 5

    --------------------------------------------------

    Final Check:
        return max_profit
        return 5

        This means:
            The best single trade is buy at 1 and sell at 6, for a profit of 5.




---
🧠 First Time? Thoughts → Code

Read the problem (10 sec)
    • Pick one buy day and one later sell day — maximize sell price minus buy price.

    • If no profit is possible, return 0.

    • Key constraint: buy must come before sell. You can't sell then buy.


Start naive (totally fine)
    • Try every buy day i, then every sell day j after it. Track the biggest profit.
        → Nested loops over all pairs.

    • O(N²) time — fine for small inputs, too slow for big arrays.


The one insight that unlocks the optimal code
    • You don't need to try every buy day. At any sell day, the best buy is always the lowest price seen so far.

    • Walk left to right: update the cheapest buy, then ask "if I sell today, what's my profit?"

    • Keep the best profit seen — that's your answer.

    • One pass replaces all pair checks.


Why a running minimum?
    • The array is ordered by time — you can only look backward for buys.

    • `min_price` = "cheapest day I could have bought on before today."

    • `p - min_price` = profit if you bought at that cheapest day and sold today.


Thought → line of code
    • `min_price = float('inf')`
        → Need a starting min before any price exists.
        → `inf` guarantees the first real price becomes the min without special-casing `prices[0]`.
        → (Weird syntax alert: `float('inf')` is just Python's way of saying "infinity.")

    • `max_profit = 0`
        → Start at 0 because "no profit" is the default answer.
        → We only update when we actually find a gain.

    • `for p in prices:`
        → One left-to-right scan — time order is built into the array.

    • `if p < min_price: min_price = p`
        → New low? That's the new best buy point going forward.

    • `profit = p - min_price`
        → The core question: "sell today after buying at the cheapest day so far."

    • `if profit > max_profit: max_profit = profit`
        → Save the best sell day we've seen so far.

    • `return max_profit`
        → Never found profit? Still 0. Found one? Return the best.


Memory hook (one sentence)
    • Walk the prices, remember the cheapest buy, and track the best "sell today" profit.


Would you arrive at this cold?
    • Immediately: nested loops — "try every buy, then every sell after it." You'd probably get O(N²) without studying.

    • After asking "what does the input buy me?": the array is already in time order, so you only need the running minimum — not every past day.

    • Bookkeeping: `min_price`, `max_profit`, the update checks.

    • Real insight: at each day, the optimal buy is always the min so far — that's what kills the inner loop.







---
Q: Why do we use `float('inf')` in this solution?

A: We need to track the minimum price, and starting at +∞ guarantees the first real price becomes the new minimum.

  • It avoids awkward edge cases like manually doing `min_price = prices[0]`.
      • Empty list → prices[0] crashes.

  • Makes the logic cleaner: every upcoming price is compared against an initial "impossibly large" value.

  • Ensures the algorithm works even if prices change later or input formats vary — the first number will always replace +∞.


"""




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
# Brute Force: Check Every Possible Buy-Sell Day
def maxProfit(prices):
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

