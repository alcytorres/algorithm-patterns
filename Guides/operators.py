# Python Operators Cheat Sheet

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


# Plain English
| Op | In simple terms                        | Example     |
|----|----------------------------------------|-------------|
| +  | Put two numbers together               | 5 + 3 = 8   |
| -  | Take one number away from another      | 5 - 3 = 2   |
| *  | Multiply two numbers                   | 5 * 3 = 15  |
| /  | Divide — answer keeps decimals         | 5 / 2 = 2.5 |
| // | Divide — chop off decimals (int only)  | 5 // 2 = 2  |
| %  | Leftover after divide (remainder)      | 5 % 2 = 1   |
| ** | Number multiplied by itself (power)    | 2 ** 3 = 8  |


# =============================================================================
# // and % — LeetCode essentials (read this once, reuse forever)
# =============================================================================
#
# Both come from the SAME question:
#   "How many WHOLE times does the bottom number fit into the top?"
#
#   a = (b × whole times) + leftover
#
#   //  →  keep the whole times
#   %   →  keep the leftover
#
# NOT decimal division.  17 / 10 = 1.7  but  17 // 10 = 1  and  17 % 10 = 7


# --- % (modulo) — the leftover ---

| Expression | Whole times 10 fits | Breakdown           | Result |
|------------|---------------------|---------------------|--------|
| 1 % 10     | 0                   | 1 = 10×0 + 1        | 1      |
| 17 % 10    | 1                   | 17 = 10×1 + 7       | 7      |
| 19 % 10    | 1                   | 19 = 10×1 + 9       | 9      |
| 123 % 10   | 12                  | 123 = 10×12 + 3     | 3      |

Shortcut:  n % 10  =  last digit of n
    123 % 10 = 3     456 % 10 = 6     789 % 10 = 9


# --- // (floor division) — the whole times (drop the leftover) ---

| Expression | Question                    | NOT this        | Result |
|------------|-----------------------------|-----------------|--------|
| 1 // 10    | How many whole 10s in 1?    | 1 / 10 = 0.1    | 0      |
| 17 // 10   | How many whole 10s in 17?   | 17 / 10 = 1.7   | 1      |
| 19 // 10   | How many whole 10s in 19?   | 19 / 10 = 1.9   | 1      |
| 123 // 10  | How many whole 10s in 123?  | 123 / 10 = 12.3 | 12     |

Shortcut:  n // 10  =  drop the last digit
    123 // 10 = 12     456 // 10 = 45     789 // 10 = 78


# --- // and % together — peel digits from a number ---

Same number, two answers from one split:

    19  =  (19 // 10) × 10  +  (19 % 10)
    19  =       1       × 10  +       9
          ↑ whole part          ↑ last digit

Walkthrough (n = 19):
| Step  | Code     | n % 10 (grab) | n // 10 (drop) | n after |
|-------|----------|---------------|----------------|---------|
| start | n = 19   | —             | —              | 19      |
| 1     | n % 10   | 9             | —              | 19      |
| 2     | n // 10  | —             | remove 9       | 1       |
| 3     | n % 10   | 1             | —              | 1       |
| 4     | n // 10  | —             | remove 1       | 0 stop  |

Code template (Happy Number, Reverse Integer, Add Digits, etc.):
    while n > 0:
        digit = n % 10    # grab last digit
        # ... use digit ...
        n //= 10          # drop last digit


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

"""

