"""
Guide to Solving Sliding Window Problems

# Key Strategies
1. **Fixed-Size Window**: Use for problems with a constant window size (e.g., max sum of k elements).
2. **Variable-Size Window**: Adjust window size dynamically based on conditions (e.g., subarrays with sum k).
3. **Efficient Updates**: Update window sum or count by adding new elements and removing old ones without recalculating.
4. **Condition Checks**: Monitor window properties (sum, count, etc.) to meet problem requirements.
5. **Edge Case Handling**: Manage cases like empty arrays or insufficient elements.

# Key Plan in Your Head
1. **Identify Window Type**: Fixed-size for known lengths, variable-size for condition-based lengths.
2. **Initialize Window**: Set up initial sum, count, or other trackers.
3. **Slide the Window**: Use loops to move the window across the array or string.
4. **Update Window**: Add new elements and remove old ones efficiently.
5. **Check Conditions**: Verify if the current window meets the problem's criteria.
6. **Handle Edges**: Check for invalid inputs or windows larger than the array.

# Key Lines of Code to Know
1. **Initialize Window**:
   window_sum = sum(arr[:k])  # Fixed-size
   vowel_count = 0  # Variable-size
   
2. **Slide the Window**:
   for i in range(k, len(arr)):  # Fixed-size
   for right in range(len(s)):  # Variable-size
   
3. **Update Window**:
   window_sum = window_sum - arr[i - k] + arr[i]  # Fixed-size
   if s[right] in vowels: vowel_count += 1  # Variable-size
   
4. **Shrink Window (Variable-Size)**:
   while window_sum > k and left <= right:
       window_sum -= arr[left]
       left += 1
       
5. **Check Conditions**:
   if window_sum == k: count += 1
   if vowel_count <= k: max_length = max(max_length, right - left + 1)
   
6. **Handle Edge Cases**:
   if len(arr) < k: return None

# Other Key Notes
- **Efficiency**: Typically O(n) time by avoiding nested loops.
- **Space**: Usually O(1), excluding output.
- **Applicability**: Ideal for contiguous subarray/substring problems.
- **Visualization**: Imagine a moving frame that maintains relevant data within its bounds.
"""
