class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack, closingLookup = [], {'(': ')', '{': '}', '[': ']'}
        for a_chr in s:
            # If opening bracket: push to stack
            if a_chr in closingLookup: stack.append(a_chr)
            # If closing: if top of the stack doesn't have a matching opening bracket, return false
            elif not stack or closingLookup[stack[-1]] != a_chr: return False
            # Else: we have a matching brackets, continue 
            else:
                stack.pop()
        # Must empty the stack (no opening brackets left)
        return not stack
        