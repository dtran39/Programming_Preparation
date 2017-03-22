'''
Problem:
	- Given a non-empty string 
		check if it can be constructed by 
			taking a substring of it and appending multiple copies of the substring together. 

----------------------------------------------------------------------------------------------------
Examples: 
	Example 1:	Input: "abab"			Output: true 		Explanation: It's the substring "ab" twice.
	Example 2:  Input: "aba" 			Output: False
	Example 3:  Input: "abcabcabcabc" 	Output: True	   
		Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
----------------------------------------------------------------------------------------------------
Solution: https://discuss.leetcode.com/topic/68210/from-intuitive-but-slow-to-really-fast-but-a-little-hard-to-comprehend
Solution 1: try every substring from (0, 0) to (0, n / 2)
	Time: O(n ^ 3), Space: O(n)
Solution 2: Use the info given by failed matching (basis of KMP algorithm)
	lps[i] is the length of the longest proper prefix that is also a suffix of (s[0], ..., s[i])
		lps[0] = 0 (one character string has no proper prefix or suffix)
	Use lps to check:
		- if str = (s[0], ..., s[km - 1]) is constructed by 
			joining m copies of its substring substr = (s[0], ..., s[k-1]), 
		and assuming that substr is the finest making block str can be boiled down to, 
		meaning str is not constructed by joining copies of any proper substring of substr. 
		Then we must have lps[km - 1] equals (m - 1)k.
		- assuming that the longest proper prefix of string str that is also a suffix, 
		and the remaining string remainderStr obtained by removing prefix from str satisfies the following 3 properties:
			remainderStr is a proper substring of str,
			|str| is divisiable by |remainderStr|,
			remainderStr is a prefix of prefixStr.
	Time: O(n), space: O(n)
'''
class Solution(object):
	def repeatedSubstringPattern(self, _str):
		# Calculate lps
		strLen = len(_str)	
		def get_lps(_str):
			# Two pointers: 
			lps = [0] * strLen
			prefix_ptr, str_iterator = 0, 1
			while str_iterator < strLen:
				# If match: Store prefix_ptr + 1 (because match) on lps[str_iterator], increment both to match		
				if _str[prefix_ptr] == _str[str_iterator]:
					lps[str_iterator] = prefix_ptr + 1
					prefix_ptr, str_iterator = prefix_ptr + 1, str_iterator + 1					
				# Else
				else:
					# If there is another substring prefix that is also a suffix, jump to start checking from that
					if prefix_ptr > 0:
						prefix_ptr = lps[prefix_ptr - 1]
					# If not, there is no substring prefix that is also a suffix from str[0] to str[str_iterator]moving on
					else:
						lps[str_iterator] = 0
						str_iterator += 1
			return lps
		# get lps
		lps = get_lps(_str)
		lps_str = lps[strLen - 1]
		# Check: 
			#string must have a proper substring that is both a prefix and suffix
			# if exist a substring multiplied, then remainderStr obtained by removing prefix from str must
				# be a proper substring of str and a prefix of str
				# |str| % |remainderStr| = 0
		return lps_str > 0 and strLen % (strLen - lps_str) == 0 and _str[lps_str:] == _str[:(strLen - lps_str)]
	def repeatedSubstringPatternNaive(self, _str):
		# Base case
		strLen = len(_str)
		if strLen == 1: 
			return False
		# Normal case
		# Helper function to determine if a substring can be multiplied to a string
		def is_subStr_multiples(_str, subStr):
			subStrLen = len(subStr)
			# Short circuit
			if strLen % subStrLen != 0:
				return False
			# Loop through each substring to see if it can cover the whole string
			for i in range(strLen / subStrLen):
				if _str[i * subStrLen : i * subStrLen + subStrLen] != subStr:
					return False
			return True
		# End helper function
		for i in range(strLen / 2):
			if is_subStr_multiples(_str, _str[:i + 1]):
				return True
		return False

