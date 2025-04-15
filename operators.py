"""
Here's a concise cheat sheet for Python operators, categorized by type. I'll keep it clear and practical for quick reference:
"""

#1. Arithmetic Operators
| Operator | Description            | Example      |
|----------|------------------------|--------------|
|    +     | Addition               | `5 + 3 = 8`  |
|    -     | Subtraction            | 5 - 3 = 2    |
|    *     | Multiplication         | 5 * 3 = 15   |
|    /     | Division (float)       | 5 / 2 = 2.5  |
|    //    | Floor Division (int)   | 5 // 2 = 2   |
|    %     | Modulus (remainder)    | 5 % 2 = 1    |
|    **    | Exponentiation         | 2 ** 3 = 8   |


#2. Comparison Operators
| Operator | Description            | Example       |
|----------|------------------------|---------------|
|    ==    | Equal to               | 5 == 5 (True) |
|    !=    | Not equal to           | 5 != 3 (True) |
|    <     | Less than              | 5 < 6 (True)  |
|    >     | Greater than           | 5 > 3 (True)  |
|    <=    | Less than or equal     | 5 <= 5 (True) |
|    >=    | Greater than or equal  | 5 >= 4 (True) |


#3. Logical Operators
| Operator | Description                  | Example                |
|----------|------------------------------|------------------------|
|   and    | True if both are true        | True and False = False |
|   or     | True if at least one is true | True or False = True   |
|   not    | Inverts truth value          | not True = False       |


# 4. Assignment Operators
| Operator  | Description            | Example            |
|-----------|------------------------|--------------------|
|    =      | Assign value           | x = 5              |
|    +=     | Add and assign         | x += 3 (x = x + 3) |
|    -=     | Subtract and assign    | x -= 2 (x = x - 2) |
|    *=     | Multiply and assign    | x *= 2 (x = x * 2) |
|    /=     | Divide and assign      | x /= 2 (x = x / 2) |
|    //=    | Floor divide and assign| x //= 2            |
|    %=     | Modulus and assign     | x %= 2             |
|    **=    | Exponent and assign    | x **= 2            |


#5. Bitwise Operators
| Operator | Description            | Example       |
|----------|------------------------|---------------|
|    &     | Bitwise AND            | 5 & 3 = 1     |
|    |     | Bitwise OR             | 5 | 3 = 7     |
|    ^     | Bitwise XOR            | 5 ^ 3 = 6     |
|    ~     | Bitwise NOT            | ~5 = -6       |
|    <<    | Left shift             | 5 << 1 = 10   |
|    >>    | Right shift            | 5 >> 1 = 2    |


#6. Identity Operators
| Operator | Description             | Example                  |
|----------|-------------------------|--------------------------|
| is       | True if same object     | x is y (checks identity) |
| is not   | True if not same object | x is not y               |


#7. Membership Operators
| Operator | Description                   | Example                   |
|----------|-------------------------------|---------------------------|
| in       | True if value in sequence     | 3 in [1, 2, 3] (True)     |
| not in   | True if value not in sequence | 4 not in [1, 2, 3] (True) |


#8. Operator Precedence (Highest to Lowest)
| Operator       | Description                                |
|----------------|--------------------------------------------|
| **                          | Exponentiation                |
| ~, +, -                     | Unary plus/minus, Bitwise NOT |
| *, /, //, %                 | Multiplication, Division, Floor Division, Modulus |
| +, -                        | Addition, Subtraction         |
| <<, >>                      | Bitwise shifts                |
| &                           | Bitwise AND                   |
| ^                           | Bitwise XOR                   |
| |                           | Bitwise OR                    |
| Comparison (<, >, ==, etc.) | Comparisons                   |
| not                         | Logical NOT                   |
| and                         | Logical AND                   |
| or                          | Logical OR                    |
| Assignment (=, +=, etc.)    | Assignment                    |


"""

Notes:
- Use parentheses `()` to override precedence when needed (e.g., `(2 + 3) * 4` vs. `2 + 3 * 4`).
- Bitwise operators work on integers at the binary level.
- Membership operators are handy for strings, lists, tuples, etc.

Let me know if you’d like examples or a deeper dive into any of these!

"""

