"""
Task: Parse a string containing infix operators and values, do the math evaluation and print the result

Example input: 1 + 2 * 10  |  output: 21

Inflix operators can be only + or * or -

expr = expression 
"""


def evaluate(expr):
    # turn "1 + 2 * 10" → ['1', '+', '2', '*', '10']
    tokens = expr.split()

    # ─── First pass: fold all the multiplications ───
    folded = []
    i = 0
    while i < len(tokens):
        tok = tokens[i]
        if tok == '*':
            # pop the last number, multiply by the next, push result
            left = int(folded.pop())
            right = int(tokens[i+1])
            folded.append(str(left * right))
            i += 2  # skip over the operator and next number
        else:
            folded.append(tok)
            i += 1

    # ─── Second pass: do additions and subtractions left to right ───
    result = int(folded[0])
    i = 1
    while i < len(folded):
        op = folded[i]
        val = int(folded[i+1])
        if op == '+':
            result += val
        else:  # op == '-'
            result -= val
        i += 2  # move to the next operator

    return result

# example
print(evaluate("1 + 2 * 10"))  # 21



# ----------------------------------------------------------------------------------
# Solution with output Full Breakdown

# Task: Parse a string containing infix operators (+, -, *) and values, evaluate the expression, and return the result.
# Example: expr = "1 + 2 * 10" → Output = 21
# Why: Practices parsing and operator precedence (multiplication before addition/subtraction) without parentheses.

def evaluate(expr):  # Example: expr = "1 + 2 * 10"

    # 1️⃣ Tokenize the expression
    # Split the string into a list of tokens (numbers and operators)
    # Why? We need to process each number and operator separately
    tokens = expr.split()  # "1 + 2 * 10" → tokens = ['1', '+', '2', '*', '10']

    # 2️⃣ First pass: Fold all multiplications
    # Initialize a list to store tokens after handling multiplications
    # Why? We process * first due to operator precedence, reducing the expression
    folded = []  # folded = []
    i = 0  # index to iterate through tokens

    while i < len(tokens):  # i goes from 0 to 4 (len(tokens) = 5)
        # --- Iteration 1: i = 0 ---
        tok = tokens[i]  # tok = tokens[0] = '1'
        # Check if the current token is a multiplication operator
        # Why? We handle * by multiplying the previous and next numbers
        if tok == '*':  # tok = '1', not '*', skip to else
            # Pop the last number, multiply by the next, push result
            left = int(folded.pop())  # skip
            right = int(tokens[i+1])  # skip
            folded.append(str(left * right))  # skip
            i += 2  # skip
        else:
            # Append non-multiplication tokens (numbers or +,-) to folded
            folded.append(tok)  # folded = ['1']
            i += 1  # i = 0 + 1 = 1
        # After Iteration 1: i = 1, folded = ['1']

        # --- Iteration 2: i = 1 ---
        if i == 1:
            tok = tokens[i]  # tok = tokens[1] = '+'
            if tok == '*':  # tok = '+', not '*', skip to else
                left = int(folded.pop())
                right = int(tokens[i+1])
                folded.append(str(left * right))
                i += 2
            else:
                folded.append(tok)  # folded = ['1', '+']
                i += 1  # i = 1 + 1 = 2
            # After Iteration 2: i = 2, folded = ['1', '+']

        # --- Iteration 3: i = 2 ---
        if i == 2:
            tok = tokens[i]  # tok = tokens[2] = '2'
            if tok == '*':  # tok = '2', not '*', skip to else
                left = int(folded.pop())
                right = int(tokens[i+1])
                folded.append(str(left * right))
                i += 2
            else:
                folded.append(tok)  # folded = ['1', '+', '2']
                i += 1  # i = 2 + 1 = 3
            # After Iteration 3: i = 3, folded = ['1', '+', '2']

        # --- Iteration 4: i = 3 ---
        if i == 3:
            tok = tokens[i]  # tok = tokens[3] = '*'
            if tok == '*':  # tok = '*', true
                # Pop the last number (previous number)
                left = int(folded.pop())  # folded = ['1', '+'], pop '2', left = 2
                # Get the next number
                right = int(tokens[i+1])  # tokens[4] = '10', right = 10
                # Multiply and append result as a string
                folded.append(str(left * right))  # 2 * 10 = 20, folded = ['1', '+', '20']
                i += 2  # i = 3 + 2 = 5 (skip operator and next number)
            else:
                folded.append(tok)
                i += 1
            # After Iteration 4: i = 5, folded = ['1', '+', '20']
            # Loop exits (i = 5, len(tokens) = 5)

    # 3️⃣ Second pass: Process additions and subtractions left to right
    # Initialize result with the first number
    # Why? We start with the first number and apply + or - operations
    result = int(folded[0])  # folded[0] = '1', result = 1
    i = 1  # start at the first operator

    while i < len(folded):  # i goes from 1 to 2 (len(folded) = 3)
        # --- Iteration 1: i = 1 ---
        # Get the operator
        op = folded[i]  # op = folded[1] = '+'
        # Get the next number
        val = int(folded[i+1])  # folded[2] = '20', val = 20
        # Apply the operator
        if op == '+':  # op = '+', true
            result += val  # result = 1 + 20 = 21
        else:  # op == '-'
            result -= val  # skip
        i += 2  # i = 1 + 2 = 3 (move to next operator)
        # After Iteration 1: i = 3, result = 21
        # Loop exits (i = 3, len(folded) = 3)

    # 4️⃣ Return the final result
    # Why? result contains the evaluated value of the expression
    return result  # result = 21


print(evaluate("1 + 2 * 10"))  # Output: 21