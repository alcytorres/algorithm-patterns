"""
Guide to Solving Prefix Sum Problems

# Key Strategies
   1. Compute Prefix Sums: Create an array where each element is the sum of all previous elements plus the current one. Useful for running totals (e.g., `prefix_sum`).
   2. Use Prefix Sums for Ranges: Efficiently calculate subarray sums using `prefix[end] - prefix[start-1]` (e.g., `range_sum`).
   3. Detect Patterns: Identify subarrays with specific sums (like zero) using prefix sums and a set (e.g., `has_zero_sum_subarray`).
   4. Optimize Subarray Problems: Solve maximum or specific-sized subarray sum problems efficiently (e.g., `max_subarray_sum`).
   5. Check for Equal Sums: Split arrays into equal-sum parts by comparing prefix sums to a target (e.g., `can_partition`).

# Key Plan in Your Head
   1. Identify the Problem: Does it involve subarray sums or running totals? (e.g., range queries, zero-sum subarrays).
   2. Build Prefix Sums: If sums are needed, compute a prefix sum array.
   3. Apply Subtraction: Use `prefix[end] - prefix[start-1]` for range sums (or `prefix[end]` if starting at 0).
   4. Track Sums: Use a set to detect repeated sums or specific conditions (e.g., sum equals zero or target).
   5. Handle Edges: Check for empty arrays or invalid inputs (e.g., `if not arr: return []`).
   6. Optimize: Leverage precomputed prefix sums to avoid redundant calculations.

# Key Lines of Code to Know
1. Compute Prefix Sums:
   result = [arr[0]]  # Start with first element
   for i in range(1, len(arr)): result.append(result[-1] + arr[i])
   
2. Range Sum Query:
   if start == 0: return prefix[end]
   return prefix[end] - prefix[start - 1]
   
3. Check for Zero Sum Subarray:
   prefix_sum = 0; seen = set()
   for num in arr: 
       prefix_sum += num
       if prefix_sum == 0 or prefix_sum in seen: return True
       seen.add(prefix_sum)
   
4. Max Subarray Sum of Size K:
   prefix = prefix_sum(arr)
   max_sum = prefix[k - 1]
   for i in range(k, len(arr)): 
       current_sum = prefix[i] - prefix[i - k]
       max_sum = max(max_sum, current_sum)
   
5. Partition Array into Equal Sums:
   total_sum = sum(arr)
   if total_sum % 2 != 0: return False
   target = total_sum // 2; prefix_sum = 0
   for num in arr: 
       prefix_sum += num
       if prefix_sum == target: return True

# Other Key Notes
   - Efficiency: O(n) preprocessing for prefix sums enables O(1) range queries.
   - Space: Usually O(n) for the prefix array, but some problems can use O(1) space.
   - Edge Cases: Always handle empty arrays, single elements, or invalid inputs.
   - Visualization: Think of prefix sums as a "running total" to quickly extract subarray sums.
"""
