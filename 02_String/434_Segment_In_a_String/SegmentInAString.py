'''
Problem:
	- Count the number of segments in a string, 
		where a segment is defined to be a contiguous sequence of non-space characters.
		Please note that the string does not contain any non-printable characters.

----------------------------------------------------------------------------------------------------
Examples: 
Input: "Hello, my name is John"
Output: 5

----------------------------------------------------------------------------------------------------
Solution: 
	Loop through each character:
		Increment count if find a space after a non-space
	Caution:
		Must start from the second character (because i - 1)
		Must count the last segment (because the loop does not include)
'''
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Base case
        if not s:
            return 0
        count = 0
        for i in range(1, len(s)):
            # If meet a space, check if there is non space before it, increment count"
            if s[i] == " " and s > 0 and s[i - 1] != " ":
                print s[i - 1]
                count += 1
        # Must include the last segment
        if s[len(s) - 1] != " ":
            count += 1
        return count
