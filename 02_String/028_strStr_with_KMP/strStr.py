'''
Problem:
	- Implement strStr().
	Returns the index of the first occurrence of substr in _str, or -1 if substr is not part of _str.

----------------------------------------------------------------------------------------------------
Examples: 

----------------------------------------------------------------------------------------------------
Solution: 
1. Use built-in function:
	_str.index(substr)
1. Brute force
	Time: O(mn), space: O(1)
	Remember off - by one: strLen - substr_len + 1
2. KMP
	Time: O(n). space: O(m)

'''
class Solution(object):
	def strStr(self, _str, substr):
		# Edge cases
		if not substr: return 0
		if not _str: return -1
		str_len, substr_len = len(_str), len(substr)
		if str_len < substr_len: return -1
		# Get the lps array to store (this acts like kind of dp)
		lps = self.get_lps(substr)
		str_ptr, substr_ptr = 0, 0
		while str_ptr < str_len and substr_ptr < substr_len:
			# If two characters match, continue the matching process
			if _str[str_ptr] == substr[substr_ptr]:
				str_ptr, substr_ptr = str_ptr + 1, substr_ptr + 1
				# If matching complete: return
				if substr_ptr == substr_len:
					return str_ptr - substr_len
			# If not match: tricky
			else:
				'''
				if substr_ptr > 0: which means there is a match between 
					substr[ :substr_ptr - 1] with str[str_ptr - substr_ptr : str_ptr - 1]
				Therefore we don't have to made those comparison again, and can compare between:
					str[str_ptr] (the current character in the string) with
					substr[lps[substr_ptr - 1]]: the character after those matches
				# First try to shorten the current substr to its next longest proper prefix that is also a suffix
				# example: abcabd(str) vs abcabc (substr)  failed: we don't restart and compare last d with first a, but:
					we see that ab in substr and ab[the one before d] are already matched
					so we continue to match c (the first c in substr) with d
				# Because 
				'''
				if substr_ptr > 0:
					substr_ptr = lps[substr_ptr - 1]
				else:
					str_ptr += 1
		# Have not found anything 
		return -1 
	def get_lps(self, substr):
		'''compute lps: lps[i] is the length of longest proper prefix that is also a proper suffix of substr[0:i]'''
		substr_len =  len(substr)
		lps = [0] * substr_len
		# Because str[0: 0] is just a character -> it doesn't have a proper prefix or proper suffix -> lps[0] = 0
		# Starts from the second character: we have two pointers: prefix_ptr and suffix_ptr, always try to match those
		pre_ptr, suf_ptr = 0, 1
		while suf_ptr < substr_len:
			# Match case
			if substr[pre_ptr] == substr[suf_ptr]:
				# meaning from substr[0 : suf_ptr] exist a proper prefix that is also a proper suffix of length:
					# pre_ptr (the previous length of proper prefix that is also a suffix) + 1 (the newly matched character)
				lps[suf_ptr] = pre_ptr + 1
				# Increment both ptr to see if there are any more matches
				pre_ptr, suf_ptr = pre_ptr + 1, suf_ptr + 1
				'''Not match case: 
				The tricky one. It means we cannot continue with the current matching 
				(the match that check if substr[0 : suf_ptr] has a substr[0 : pre_ptr] that is a proper prefix and suffix)
				we have two choices'''
			else:
				''''
				If pre_ptr > 0: that means substr[0 : suf_ptr - 1] already has a proper prefix that is also a suffix
				Therefore, we could try another shorter prefix and picks up from that matching
				How do we do that: 
					by look at substr[0 : pre_ptr - 1] to see if exist any proper suffix that is also a prefix
				Ex: if acac doesn't work, go back to aca. 
					Check if there is a proper prefix that is also a suffix -> YES (a)
					Starts matching from the next character in the prefix: c (the second letter i aca) 
						with the current character in the suffix
				'''
				if pre_ptr > 0:
					pre_ptr = lps[pre_ptr - 1]
					'''	
				If pre_ptr == 0: that means we tried every shorter proper prefix and no match found
					-> COnclusion: substr[0 : suf_ptr - 1] does not have a proper prefix that is also a suffix
				-> HOPELESS substr[0:suf_ptr] has no proper prefix that is also a suffix
					+ Store that information : lps[suf_ptr] = 0
					+ Starts from beginning with a new character: 0 with suf_ptr + 1
				Therefore, we will need to start from the beginning: compare substr[suf_ptr] with substr[0]
					'''
				else:
					# pre_ptr is already 0
					lps[suf_ptr] = pre_ptr
					suf_ptr += 1
		return lps
	def strStrBuiltFn(self, _str, substr):
		try:
			return _str.index(substr)
		except:
			return -1
	def strStrBF(self, _str, substr):
	    """
	    :type _str: str
	    :type substr: str
	    :rtype: int
	    """
	    # Edge case
	    if not substr: return 0
	    if not _str: return -1
	    # normal case: loop
	    strLen, substr_len = len(_str), len(substr)
	    for i in range(strLen - substr_len + 1):
	    	found = True
	    	for j in range(substr_len):
	    		if _str[i + j] != substr[j]:
	    			found = False
	    			break
	    	if found: return i
	    return -1
	    
