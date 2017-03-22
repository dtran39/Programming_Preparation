'''
Problem:
	- Given two strings S and T, determine if they are both one edit distance apart.
	- Add a character		Delete a character		Change a character

----------------------------------------------------------------------------------------------------
Examples: 

----------------------------------------------------------------------------------------------------
Solution: 
	Check length of two strings
	If length diff > 1: false
	if length diff == 1: check if can delete one character in long to make short
	if length diff == 1: check if can change one character in long to make short (long and short are arbirary)
'''
class Solution(object):
	def isOneEditDistance(self, s, t):
		l, s = s, t
		if len(s) > len(l): l, s = s, l
		# Check length diff
		diff = len(l) - len(s) # Diff is guaranteed >= 0
		if diff == 0: return self.isOneReplace(s, l)
		if diff == 1: return self.isOneInsert(s, l)
		return False
	def isOneInsert(self, s, l):
		if not s: return True
		# Must l string must have one more additional character than s string
		# which mean if encounter different pair of characters: increment ptr of s
		for ps in range(len(s)):
		    if s[ps] != l[ps]:
		        return s[ps :] == l[ps + 1 :]
		return True
	def isOneReplace(self, s, l):
		replaced = False
		for i in range(len(l)):
			if l[i] != s[i]:
				if replaced: return False
				replaced = True
		# Must has exactly one pair of characters different
		return replaced
   
if __name__ == "__main__":
    print Solution().isOneEditDistance("a", "")
    print Solution().isOneEditDistance("a", "a")
    print Solution().isOneEditDistance("a", "b")
    print Solution().isOneEditDistance("ab", "a")
    print Solution().isOneEditDistance("ab", "dab")	
    print Solution().isOneEditDistance("teacher", "acher")