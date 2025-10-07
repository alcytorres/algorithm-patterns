"""
Here's a concise cheat sheet for truthy vs. falsy values in Python, tailored for solving LeetCode data structures and algorithms problems. It focuses on the most critical concepts for success in conditionals, loops, and data structure manipulations.

Truthy vs. Falsy in Python for LeetCode

   • In Python, truthy values evaluate to `True` and falsy values evaluate to `False` in boolean contexts (e.g., `if`, `while`). 

   • This is key for handling edge cases and writing efficient code in LeetCode problems.

"""


# Common Falsy Values
| Value       | Description                  | LeetCode Example               |
|-------------|------------------------------|--------------------------------|
| `[]`        | Empty list                   | `if not arr: return 0`         |
| `{}`        | Empty dictionary             | `if not d: return None`        |
| `''`        | Empty string                 | `if not s: return ""`          |
| `set()`     | Empty set                    | `if not seen: add(item)`       |
| `0`         | Zero (int)                   | `if not count: break`          |
| `0.0`       | Zero (float)                 | `if not val: continue`         |
| `None`      | Null value                   | `if root is None: return`      |
| `False`     | Boolean false                | `if not flag: skip()`          |

# Common Truthy Values
| Value         | Description                  | LeetCode Example               |
|---------------|------------------------------|--------------------------------|
| `[1, 2]`      | Non-empty list               | `if arr: process(arr)`         |
| `{'a': 1}`    | Non-empty dictionary         | `if d: lookup(key)`            |
| `'hello'`     | Non-empty string             | `if s: return s.upper()`       |
| `{1}`         | Non-empty set                | `if seen: check(item)`         |
| `1`, `-1`     | Non-zero integer             | `if num: compute(num)`         |
| `3.14`        | Non-zero float               | `if val: adjust(val)`          |
| `True`        | Boolean true                 | `if flag: execute()`           |


"""
Key Use Cases in LeetCode
1. Empty Checks: Use `if not x:` to handle empty lists, strings, dicts, etc.
   - Example: Early return for empty array in two-pointer problems.

2. None Checks: Common in trees/graphs.
   - Example: `if node is None:` to stop recursion.

3. Zero Handling: `0` is falsy, so use `if x == 0:` if zero is valid.
   - Example: Avoid `if not x:` when `x` can be zero in math problems.

4. Loops: Use truthy/falsy for concise conditions.
   - Example: `while stack:` to process until stack is empty.

5. Built-ins: Leverage `any()` and `all()` for collections.
   - Example: `if any(nums):` to check for non-zero elements.


Quick Tips
- Debug with bool(): `bool([])` → `False`, `bool([1])` → `True`.

- Avoid Pitfalls:
  - `''` is falsy, but `'0'` is truthy (non-empty string).
  - `0` is falsy, but `0.1` is truthy.

- Edge Cases: Test with `[]`, `0`, `None` to ensure correctness.

"""