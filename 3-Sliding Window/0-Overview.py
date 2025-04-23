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

# ----------------------------------------------------------------------------------
"""
Templates
    Fixed Sliding Window
    Dynamic Sliding Window
"""

# ----------------------------------------------------------------------------------
# Fixed-size sliding window
def sliding_window_fixed(arr, k):
    # Initialize
    window_sum = 0
    
    # Set up the initial window
    for i in range(k):
        window_sum += arr[i]
    
    max_result = window_sum  # Initialize result
    
    # Slide the window across the array
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]  # Add new element, remove old element
        max_result = max(max_result, window_sum)  # Update max_result
    
    return max_result


# ----------------------------------------------------------------------------------
# Dynamic Sliding Window

def sliding_window_variable(arr):
    left = 0
    window_state = 0  # (sum, count, frequency_map, etc.)
    min_or_max_result = float('inf')  # or float('-inf') depending on the goal
    
    for right in range(len(arr)):
        # Expand the window
        window_state += arr[right]  # Update window_state to include arr[right]
        
        # Shrink the window while the condition is violated
        while window_state > some_condition:  # Replace with actual condition
            min_or_max_result = min(min_or_max_result, window_state)  # Update result if needed
            window_state -= arr[left]  # Update window_state to exclude arr[left]
            left += 1  # Move left pointer forward
    
    return min_or_max_result

# ----------------------------------------------------------------------------------
