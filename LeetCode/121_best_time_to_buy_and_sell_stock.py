# Best Time to Buy and Sell Stock I
"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Find and return the maximum profit you can achieve.
 
Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5

Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Why: Practices tracking minimum price and maximum profit efficiently in a single pass.

https://www.youtube.com/watch?v=kJZrMGpyWpk
"""

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


# ----------------------------------------------------------------------------------

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