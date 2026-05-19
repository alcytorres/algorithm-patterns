# Ask Claude, Grok, ChatGPT to name the top 50 most common DSA problems you rec I know.
# In the prompt find a way to include the ones you already have pracitced
# Make a new weighted average list of it all



class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
        left = 0
        right = len(s) - 1
        
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        
        return s
        

solution = Solution
        s = ["h","e","l","l","o"]
        print(reversString(s))
        # Output: ["0","l","l","e","h"]
        