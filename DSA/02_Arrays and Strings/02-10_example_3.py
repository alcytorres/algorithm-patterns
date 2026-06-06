# Example 3: 713. Subarray Product Less Than K
"""
Counts subarrays where product of all elements is strictly less than k.

Example 1:
    Input: nums = [10, 5, 2, 6], k = 100
    Output: 8
    Explanation: The 8 subarrays that have product less than 100 are:
    [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
    Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

Example 2:
    Input: nums = [1, 2, 3], k = 0
    Output: 0

Example 3
    nums = [2, 3], k = 7
    Output: 3 --> [2], [2, 3], [3]

Constraints:
    1 <= nums.length <= 3 * 104
    1 <= nums[i] <= 1000
    0 <= k <= 106

Solution: https://leetcode.com/problems/subarray-product-less-than-k/
"""

# Sliding Window: Shrink Window When Product Reaches k

def num_subarrays_product_less_than_k(nums, k):
    if k <= 1:     
        return 0
    
    l = ans = 0          
    curr = 1          
    
    for r in range(len(nums)):  
        curr *= nums[r]        
        
        while curr >= k:           
            curr //= nums[l]    
            l += 1           
            
        ans += r - l + 1  
    
    return ans

nums = [10, 5, 2, 6]
k = 100
print(num_subarrays_product_less_than_k(nums, k))  
# Output: 8
# r=0: Counted [10]
# r=1: Counted [10, 5], [5]
# r=2: After shrinking, counted [5, 2], [2]
# r=3: Counted [5, 2, 6], [2, 6], [6]


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Breakdown
def num_subarrays_product_less_than_k(nums, k):
    if k <= 1:            # No valid subarray when k is 0 or 1
        return 0          # Nothing can be strictly less than k
    
    l = ans = 0           # Left edge of window; running count of valid subarrays
    curr = 1              # Product inside the current window (empty starts at 1)
    
    for r in range(len(nums)):   # Grow window by including each new right element
        curr *= nums[r]          # Multiply in the new number at the right
        
        while curr >= k:         # Shrink from the left while product is too big
            curr //= nums[l]     # Divide out the leftmost number we are dropping
            l += 1               # Move left pointer one step to the right
            
        ans += r - l + 1         # Every subarray ending at r with left in [l..r] works
    
    return ans                   # Total count of valid subarrays


"""
Time: O(N)
  - Let N = length of nums.
  - Right pointer r moves through the array once → N steps.
  - Left pointer l only moves forward (never backward).
  - Each element is multiplied in once and divided out at most once → at most 2N window updates total.
  - Each step inside the loop is O(1) (multiply, divide, add to ans).
  - Overall: O(N).


Space: O(1)
  - Only a few variables: l, ans, curr, and the loop index r.
  - No extra arrays or hash maps.
  - Overall: O(1).


Interview Answer: Worst Case

Time: O(N)
  - Sliding window — each index enters and leaves the window at most once.

Space: O(1)
  - Constant extra variables only.


---
Overview for Each Iteration
Input: nums = [10, 5, 2, 6], k = 100
Step: Count subarrays with product < k using sliding window
r | nums[r] | curr | l | curr >= k | Action                    | ans
--|---------|------|---|-----------|---------------------------|-----
- | -       | 1    | 0 | -         | -                         | 0
0 | 10      | 10   | 0 | No        | ans+=0-0+1=1              | 1
1 | 5       | 50   | 0 | No        | ans+=1-0+1=2              | 3
2 | 2       | 100  | 0 | Yes       | curr//=nums[0]=100//10=10 | 3
  |         | 10   | 1 | No        | ans+=2-1+1=2              | 5
3 | 6       | 60   | 1 | No        | ans+=3-1+1=3              | 8

Final: 8 ([10], [5], [5, 2], [2], [2, 6], [6], [10, 5], [5, 2, 6])



---
Most IMPORTANT thing to Understand:
    • Count every **contiguous** subarray whose product is **strictly less than** k.

    • Use a sliding window: expand with `r`, shrink from `l` when the product is too big (`curr >= k`).

    • `curr` = product of all numbers in the window `[l..r]`.

    • After the window is valid (`curr < k`), add `r - l + 1` — that is how many good subarrays **end at** `r`.

---
Why this code Works:
    • Sliding window:
        • `r` adds `nums[r]` to the window (multiply into `curr`).
        • `while curr >= k`: drop `nums[l]` (divide out) and move `l` right until product < k again.

    • Counting trick (`ans += r - l + 1`):
        • If `[l..r]` is valid, then `[l..r]`, `[l+1..r]`, … `[r..r]` all have product < k.
        • That is exactly `r - l + 1` subarrays ending at `r`.

    • Efficiency:
        • Brute force checks every subarray → O(N²).
        • Each index enters and leaves the window at most once → O(N).

    • Intuition:
        • Like a stretchy window on the array — pull right to grow, pinch left when the product hits k.

---
TLDR:
    • Grow the window with `r`, shrink with `l` while product ≥ k, then add how many valid subarrays end at `r`.


---
Quick Example Walkthrough:

    nums = [10, 5, 2, 6], k = 100

    r=0: curr=10 < 100 → add 1 → ans=1  ([10])

    r=1: curr=50 < 100 → add 2 → ans=3  ([10,5], [5])

    r=2: curr=100 → shrink (drop 10), curr=10, l=1 → add 2 → ans=5  ([5,2], [2])

    r=3: curr=60 < 100 → add 3 → ans=8  ([5,2,6], [2,6], [6])

    Final Answer: 8


---
Full Example Walkthrough:
    nums = [10, 5, 2, 6], k = 100

    Starting State:
        l = 0, ans = 0, curr = 1

    --------------------------------------------------

    Loop Iteration 1 (r = 0):
        Add nums[0] = 10:
            curr = 1 * 10 = 10

        curr >= k? → 10 >= 100 → NO (no shrink)

        Count:
            ans += 0 - 0 + 1 = 1

        Now:
            l = 0, curr = 10, ans = 1
            Valid endings at r=0: [10]

    --------------------------------------------------

    Loop Iteration 2 (r = 1):
        Add nums[1] = 5:
            curr = 10 * 5 = 50

        curr >= k? → NO

        Count:
            ans += 1 - 0 + 1 = 2 → ans = 3

        Now:
            l = 0, curr = 50, ans = 3
            Valid endings at r=1: [10,5], [5]

    --------------------------------------------------

    Loop Iteration 3 (r = 2):
        Add nums[2] = 2:
            curr = 50 * 2 = 100

        curr >= k? → YES → shrink:
            curr //= nums[0] → 100 // 10 = 10, l = 1

        curr >= k? → 10 >= 100 → NO

        Count:
            ans += 2 - 1 + 1 = 2 → ans = 5

        Now:
            l = 1, curr = 10, ans = 5
            Window [5,2]; valid endings: [5,2], [2]

    --------------------------------------------------

    Loop Iteration 4 (r = 3):
        Add nums[3] = 6:
            curr = 10 * 6 = 60

        curr >= k? → NO

        Count:
            ans += 3 - 1 + 1 = 3 → ans = 8

        Now:
            l = 1, curr = 60, ans = 8
            Valid endings at r=3: [5,2,6], [2,6], [6]

    --------------------------------------------------

    Final Check:
        return ans → 8

        Eight contiguous subarrays have product strictly less than 100.





---
🧠 First Time? Thoughts → Code

Read the problem (10 sec)
    • Count how many **contiguous** subarrays have product **strictly less than** k.

    • All `nums[i] >= 1` — product only grows as the window gets longer (no negatives, no zeros).

    • If k ≤ 1, nothing works → return 0 early.

Start naive (totally fine)
    • For every start `i`, extend to every end `j`, multiply elements, count if product < k.

    • O(N²) — totally reasonable first try (you already have this as brute force).

The one insight that unlocks the optimal code
    • Don't re-count from scratch for every subarray — keep one window `[l..r]` and a running product `curr`.

    • When `curr >= k`, shrink from the left (`curr //= nums[l]`, `l += 1`) until valid again.

    • At each `r`, every valid subarray **ending at r** is counted in one shot: `ans += r - l + 1`.

Why sliding window? (only if needed)
    • Contiguous subarrays = a window that only grows right and shrinks left (never reset `l` backward).

    • Positive numbers → once product ≥ k, extending further only makes it worse — safe to drop from the left.

    • `r - l + 1` is the non-obvious part — you're counting **endings**, not listing each subarray.

Thought → line of code
    • `if k <= 1: return 0`
        → Can't be strictly less than 0 or 1 with positive ints.

    • `curr = 1`
        → Empty window product (multiply in as you grow).

    • `curr *= nums[r]`
        → Include the new right end.

    • `while curr >= k: curr //= nums[l]; l += 1`
        → Window too big — remove left until product < k.

    • `ans += r - l + 1`
        → All subarrays ending at `r` with start from `l` to `r` are valid.

Memory hook (one sentence)
    • Grow `r`, shrink `l` while product ≥ k, add `r - l + 1` each step.

Would you arrive at this cold?
    • Immediately: nested loops / brute force — yes.

    • Sliding window with multiply/divide: maybe, if you've seen variable-size windows.

    • `ans += r - l + 1`: usually **not** — that's the LeetCode trick; brute force doesn't need it.

    • `curr //= nums[l]` when shrinking: makes sense once you know you're maintaining a running product.


---
Q: Why does left += 1 occur inside the if curr >= k: condition?
    • Only adjust when product is too big (curr >= k)

    • Divide out nums[left] to drop the leftmost element.
    
    • Move left forward to shrink the window.
    
    • Ensures the window's product stays < k so all valid subarrays are counted.

"""




# –––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Brute force — try every subarray (nested loops)

def num_subarrays_product_less_than_k_bruteforce(nums, k):
    if k <= 1:
        return 0

    ans = 0

    for i in range(len(nums)):       # Start of subarray
        curr = 1
        for j in range(i, len(nums)):  # End of subarray
            curr *= nums[j]            # Product of nums[i..j]
            if curr < k:
                ans += 1
            else:
                break                  # Product only grows (nums[j] >= 1), stop extending

    return ans


nums = [10, 5, 2, 6]
k = 100
print(num_subarrays_product_less_than_k_bruteforce(nums, k))
# Output: 8 → Check every subarray starting at i; count if product < k


"""
Time: O(N²)
  - Let N = length of nums.

  - Outer loop: pick start index i → O(N).

  - Inner loop: extend end index j from i → at most N steps per i.

  - Each step: multiply one number and compare → O(1).

  - Combined: O(N × N).
  - Overall: O(N²).


Space: O(1)
  - Only ans, curr, and loop indices (i, j).
  - Overall: O(1).


Interview Answer: Worst Case

Time: O(N²)
  - Every start index i tries all end indices j (until product hits k).

Space: O(1)
  - No extra arrays — just a running product.


---
Overview for Each Iteration
Input: nums = [10, 5, 2, 6], k = 100

    i=0: [10]→10✓, [10,5]→50✓, [10,5,2]→100✗ stop
    i=1: [5]→5✓, [5,2]→10✓, [5,2,6]→60✓
    i=2: [2]→2✓, [2,6]→12✓
    i=3: [6]→6✓

    ans = 2+3+2+1 = 8

Final: 8
"""




# ––––––––––––––––––––––––––––––––––––––––––––––––––
# Super simple demo of sliding window with multiplication and division
nums = [2, 4, 5]  # Basic array
curr = 1          # Start with product = 1
print("Initial curr:", curr)  # Output: 1

# Add elements to window (multiply)
curr *= nums[0]   # Include nums[0] (2), curr = 1 * 2
print("After curr *= nums[0]:", curr)  # Output: 2
curr *= nums[1]   # Include nums[1] (4), curr = 2 * 4
print("After curr *= nums[1]:", curr)  # Output: 8
curr *= nums[2]   # Include nums[2] (5), curr = 8 * 5
print("After curr *= nums[2]:", curr)  # Output: 40

# Remove element from window (divide)
curr //= nums[0]   # Remove nums[0] (2), curr = 40 / 2
print("After curr //= nums[0]:", curr)  # Output: 20.0
curr //= nums[1]   # Remove nums[1] (4), curr = 20 / 4
print("After curr //= nums[1]:", curr)  # Output: 5.0
curr //= nums[2]   # Remove nums[2] (5), curr = 20 / 5
print("After curr //= nums[2]:", curr)  # Output: 1.0

