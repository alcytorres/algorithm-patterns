# Time and Space Complexity with Big O Notation
# DSA Course in Python Lecture 1
# Video: https://www.youtube.com/watch?v=aWKEBEg55ps&list=PLKYEe2WisBTFEr6laH5bR2J19j7sl5O8R

# Overview
# --------
# This guide covers time and space complexity, focusing on Big O notation, which measures the efficiency of algorithms.

# Big O notation: A way to measure how an algorithm's performance (time or space) grows as input size increases.

# The "O" in Big O Notation stands for "order of," referring to the order of magnitude of an algorithm's worst-case growth rate for time or space as input size increases.

# Time Complexity: How long an algorithm takes to run, measured by the number of operations relative to input size.
# Space Complexity: How much memory an algorithm uses, measured by the storage needed relative to input size.

# We typically analyze the worst-case scenario, focusing on the strongest (most dominant) component of complexity.

# 1. Introduction to Time and Space Complexity
# --------------------------------------------
# Time complexity measures the number of operations an algorithm performs relative to the input size (n).
# Space complexity measures the amount of memory used.
# Big O notation describes the upper bound of an algorithm's growth rate.
    # Upper bound: Shows the worst-case scenario—how slow or resource-heavy it could get.
    # Simply: It tells you how "bad" things could get as the problem gets bigger, helping compare algorithms.

# Example 1: Squaring Numbers in an Array (O(n) Time, O(n) or O(1) Space)
# ------------------------------------------------------------------------
# Task: Given an array of n numbers, return a new array with the squares of those numbers.
# Input:  A = [1, 2, 3, 4, 5]
# Output: B = [1, 4, 9, 16, 25]

def square_array(arr):
    # Create a new array to store squared values
    result = []
    for num in arr:
        result.append(num * num)  # Square each number
    return result

# Time Complexity: O(n)
# - We loop through all n elements once, performing one operation per element.
# - The number of operations grows linearly with n.

# Space Complexity: O(n)
# - We create a new array of size n to store the results.

# Alternative: Modify the original array in-place for O(1) space complexity.
    # 8:45
def square_array_inplace(arr):
    for i in range(len(arr)):
        arr[i] = arr[i] * arr[i]  # Square each number in-place
    return arr

# Time Complexity: O(n)
# - Same as before

# Space Complexity: O(1)
# - No additional array is created; we modify the input array.
# - Constant space, as memory usage does not depend on n.


# Example 2: Finding All Pairs of Numbers (O(n^2) Time)
# -----------------------------------------------------
# Task: Given an array of n numbers, return all unique pairs of numbers.
# Input: A = [1, 2, 3, 4, 5]
# Output: [(1,2), (1,3), (1,4), (1,5), (2,3), (2,4), (2,5), (3,4), (3,5), (4,5)]

def find_all_pairs(arr):
    pairs = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):  # Start from i+1 to avoid duplicates
            pairs.append((arr[i], arr[j]))
    return pairs

# Time Complexity: O(n^2)
# - Nested loops: for each of n elements, we iterate over up to n-1 remaining elements.
# - Total operations: roughly n * n = n^2 (quadratic time).
# - This is significantly slower than O(n) for large n.

# Space Complexity: O(n^2)
# - In the worst case, we store approximately n(n-1)/2 pairs.


# 2. Understanding Big O Notation
# -------------------------------
# Big O notation describes the worst-case growth rate of an algorithm.

# Key Question: Can you find a function (like n or n²) that always grows at least as fast as your algorithm’s time or space use for large inputs? 
# - If yes, that function sets your Big O complexity, capping how bad your algorithm gets.

# If you can you draw a function (line, curve) that is always worse (higher) than your algorithm's performance for large inputs then your algorithm's complexity is bounded by that function AKA it can't be that function (n²).


# Example: Algorithm sums n numbers (takes n steps). n is the tightest function always ≥ n steps, so Big O is O(n).

def sum_array(arr):
    total = 0
    for num in arr:  # Loops n times
        total += num  # Constant-time operation
    return total

# Time:  O(n) - Loops through n elements once
# Space: O(1) - Only uses a single variable (total) regardless of input size n.


# Visualizing Complexity
# - X-axis: N: Input size (n)
# - Y-axis: Time: Number of operations (not milliseconds)
# - O(n): Linear function (straight line)
# - O(n^2): Quadratic function (parabola, steeply increasing)
# - O(n^3): Cubic function (even steeper)

# Example: Linear vs. Quadratic
# - Squaring numbers (O(n)): Operations grow linearly, forming a straight line.
# - Finding pairs (O(n^2)): Operations grow quadratically, forming a parabola.
# - O(n^2) is much slower than O(n) for large n.


# 3. Constant Time and Space Complexity (O(1))
# --------------------------------------------
# Constant time: Operations are independent of input size n.
# Constant space: Memory usage does not grow with n.

# Input: A = [1, 2, 3, 4, 5]

# Example: Get the First Element of an Array
def get_first_element(arr):
    return arr[0]  # Access the first element

# Time Complexity: O(1)
# - Accessing an array element by index takes constant time, regardless of array size.
# - Even accessing the first k elements (e.g., first 3) is O(1), as k is fixed.

# Space Complexity: O(1)
# - Uses no extra space, only returns the element directly.

# Example: Get the First Three Elements
def get_first_three_elements(arr):
    return [arr[0], arr[1], arr[2]]  # Access first three elements

# Time Complexity: O(1)
# - Three operations, independent of n.

# Space Complexity: O(1)
# - Returns a fixed-size list (3 elements), independent of n.

# Example: Print a Single Number
def print_number():
    print(5)  # Print a fixed value

# Time Complexity: O(1)
# - Single operation, independent of any input size.

# Space Complexity: O(1)
# - Uses no extra space, just prints a fixed value.


# 4. Common Big O Complexities and Examples
# ----------------------------------------
# Ordered from fastest to slowest:
# - O(1): Constant time (e.g., array indexing, hashing, printing a single value)
# - O(log n): Logarithmic time (e.g., binary search)
# - O(n): Linear time (e.g., looping through an array)
# - O(n log n): Linearithmic time (e.g., efficient sorting algorithms like quicksort)
# - O(n^2): Quadratic time (e.g., nested loops for all pairs)
# - O(n^3): Cubic time (e.g., triple nested loops for all triplets)
# - O(2^n): Exponential time (e.g., recursive algorithms for combinatorial problems)
# - O(n!): Factorial time (e.g., brute-force traveling salesman problem)

# Example: Print All Numbers in an Array
def print_all_numbers(arr):
    for num in arr:
        print(num)  # Print each number

# Time Complexity: O(n)
# - Loops through n elements, performing one print per element.

# Space Complexity: O(1)
# - Uses no extra space, just iterates and prints each element.


# 5. Mathematical Rules of Big O Notation
# ---------------------------------------
# - Focus on the strongest (most dominant) term.
# - Drop constants and lower-order terms.
# Example: If an algorithm has complexity O(5n^2 + 2n + 1):
# - Dominant term: 5n^2
# - Reduced to: O(n^2)
# - Constants (e.g., 5) and lower terms (2n, 1) are ignored, as they become negligible for large n.

# Example: Combined Operations
def complex_function(arr):
    # O(n^2): Find all pairs
    pairs = find_all_pairs(arr)
    # O(n): Print all numbers
    print_all_numbers(arr)
    # O(n): Square all numbers
    square_array(arr)
    # O(1): Print a single number
    print_number()
    return pairs

# Time Complexity: O(n^2)
# - Components: O(n^2) + O(n) + O(n) + O(1)
# - Dominant term: O(n^2)
# - Constants and lower terms (e.g., 2n) are dropped.

# 6. Space Complexity Considerations
# ----------------------------------
# - O(n) space: Creating a new array of size n (e.g., square_array).
# - O(1) space: Modifying in-place or using fixed memory (e.g., square_array_inplace).
# - O(n^2) space: Storing all pairs in an array.

# 7. Practical Insights
# ---------------------
# - Constant time (O(1)) is ideal for operations like array indexing or hashing.
# - Linear time (O(n)) is common for single-pass algorithms.
# - Quadratic time (O(n^2)) often indicates brute-force solutions; seek optimizations.
# - Logarithmic time (O(log n)) is highly efficient, seen in algorithms like binary search.
# - Always aim for the lowest possible complexity, but some problems require higher complexities (e.g., O(n^2) or O(n^3)).

# 8. Conclusion
# -------------
# Big O notation helps us compare algorithms by focusing on their worst-case performance.
# Understanding time and space complexity is crucial for writing efficient code.
# Use this guide to analyze algorithms, predict performance, and optimize solutions.

# Key Takeaways:
# - Time is measured in operations, not milliseconds.
# - Big O asks: Can you draw a worse function that bounds your algorithm?
# - Constant time (O(1)) is independent of n.
# - Focus on the strongest component (e.g., n^2 in n^2 + 2n + 1).
# - Optimize for both time and space when possible.

# End of Guide
# ------------
# Experiment with the provided functions to deepen your understanding.