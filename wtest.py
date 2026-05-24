# Ask Claude, Grok, ChatGPT to name the top 50 most common DSA problems you rec I know.
# In the prompt find a way to include the ones you already have pracitced
# Make a new weighted average list of it all



# Organize mini guides doc. Delete the bottom part that says delete

# how do you know to do this ans = [0] * n   ?
# its not something intuitive. be realistic how you would think of that or if thats just comes down to memory?

# Review slicing arrays




# update full breakdown guide. dont talk about time or space compelxicty. i already have a custom gpt for that.



def is_palindrome(s):
    cleaned = ""
    for c in s:
        if c.isalnum():
            cleaned += c.lower()

    return cleaned == cleaned[::-1]

s = "A man, a plan, a canal: Panama"
print(is_palindrome(s))


"""
Time: O(N)
  - Let N = length of the input string s.
  - First loop filters and lowercases characters into new_string → O(N).
  - Two pointers scan new_string from both ends → at most N/2 comparisons → O(N).
  - Overall: O(N).



Time: O(N)
  - Let N = length of the original string s.
  - Step 1: Build cleaned string by filtering and lowercasing each character → O(N).
      • Note: new_string += c creates a new string each time (strings can't be changed in place).

        In theory each append copies the whole string → O(N) per append → O(N²) total.
        In practice Python optimizes this, and using a list + join avoids it entirely.
        For interviews: safe to say O(N).








  - Step 1: Build a cleaned, lowercase string by scanning s once → O(N).
      • Checking c.isalpha() / isdigit() is O(1).

            • Appending with new_string = new_string + c is technically O(N) each time (strings are immutable), but for complexity study we treat this as O(N) total if rewritten with a list.



Q: Why can't string be changed in place?

Strings are immutable

"""



# Why += on Strings is O(N²) and How List + Join Fixes It

# String += (copies entire string each time)
new_string = ""
new_string += "a"   # creates "a"          (copies 1 char)
new_string += "b"   # creates "ab"         (copies 2 chars)
new_string += "c"   # creates "abc"        (copies 3 chars)
# Each += rebuilds from scratch → 1 + 2 + 3 + ... + N = O(N²)


# List + join (appends in place, joins once)
chars = []
chars.append("a")   # ["a"]               (O(1))
chars.append("b")   # ["a", "b"]          (O(1))
chars.append("c")   # ["a", "b", "c"]     (O(1))
result = "".join(chars)  # "abc"           (one O(N) pass)
# Total: N appends at O(1) + one join at O(N) = O(N)




