"""
Guide to Solving Prefix Sum Problems

# Key Strategies
1. **Identify the Goal**: Determine what the problem asks for—running totals (e.g., `prefix_sum`), range sums (e.g., `range_sum`), or subarray properties (e.g., `has_zero_sum_subarray`, `max_subarray_sum`).
2. **Build Prefix Sums**: Create an array or running total of cumulative sums to avoid recalculating sums repeatedly.
3. **Use Efficiently**:
   - Range sums: Subtract prefix sums for O(1) queries.
   - Subarrays: Track sums or use sliding windows for contiguous segments.
4. **Handle Edge Cases**: Check for empty arrays, invalid indices, or arrays shorter than required lengths.
5. **Optimize with Data Structures**: Use sets to track seen sums (e.g., for zero-sum subarrays).

# Key Plan in Your Head
1. **Classify the Problem**: Is it a cumulative sum, range query, or subarray task?
2. **Prepare Prefix Sums**: Build the prefix array or track a running sum.
3. **Solve Efficiently**:
   - Range sums: Use subtraction (`prefix[end] - prefix[start - 1]`).
   - Subarrays: Check conditions (e.g., zero sum) or slide a window.
4. **Test Boundaries**: Validate inputs and edge cases.

# Key Lines of Code to Know
1. **Build Prefix Sum Array**:
   result = [arr[0]]
   for i in range(1, len(arr)): result.append(result[-1] + arr[i])
   # Edge case: if not arr: return []

2. **Range Sum**:
   if start == 0: return prefix[end]
   return prefix[end] - prefix[start - 1]

3. **Zero-Sum Subarray**:
   prefix_sum = 0; seen = set()
   for num in arr: 
       prefix_sum += num
       if prefix_sum == 0 or prefix_sum in seen: return True
       seen.add(prefix_sum)

4. **Max Subarray Sum (Size k)**:
   if len(arr) < k: return None
   prefix = prefix_sum(arr)
   max_sum = prefix[k - 1]
   for i in range(k, len(arr)): max_sum = max(max_sum, prefix[i] - prefix[i - k])

5. **Sliding Window Average**:
   if len(arr) < k: return []
   window_sum = sum(arr[:k])
   averages = [window_sum / k]
   for i in range(k, len(arr)): 
       window_sum = window_sum - arr[i - k] + arr[i]
       averages.append(window_sum / k)

# Other Key Notes
- **Time Efficiency**: Building prefix sums is O(n); queries can be O(1).
- **Space**: O(n) for arrays, reducible to O(1) with running sums.
- **Visualization**: Think of prefix sums as a cumulative total you can "slice" for answers.
"""

