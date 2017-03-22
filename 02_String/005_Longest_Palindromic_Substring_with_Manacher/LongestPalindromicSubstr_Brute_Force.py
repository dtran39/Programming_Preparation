'''
Problem:
    - Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

----------------------------------------------------------------------------------------------------
Examples: 
    Input: "babad"              Output: "bab"
        Note: "aba" is also a valid answer.
    Input: "cbbd"               Output: "bb"
----------------------------------------------------------------------------------------------------
Solution: 
    Brute force: O(n ^ 3):
        Pick all substring, check if it is palindromic. Get the max
        Time: O(n ^ 3), space: O(n)
    DP:
        Recursive step:
        If we already knew that “bab” is a palindrome, 
            it is obvious that “ababa” must be a palindrome 
                since the two left and right end letters are the same
        Define P[ i, j ] ← true iff the substring Si … Sj is a palindrome, otherwise false.
        Base case: P[ i, i ] ← true         P[ i, i+1 ] ← ( Si = Si+1 )
        Time: O(n ^ 2), space: O(n ^ 2)
'''
# http://leetcode.com/2011/11/longest-palindromic-substring-part-ii.html
class Solution(object):
    def longestPalindromeBruteForce(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_lps_left, max_lps_right = 0, 0
        # Get each substring
        for left in range(len(s)):
            for right in range(left, len(s)):
                # Check palindomic: two pointers
                is_palindromic = True
                begin, end = left, right
                while begin < end:
                    if s[begin] != s[end]:
                        is_palindromic = False
                        break
                    begin, end = begin + 1, end - 1
                # If matched, compare length with longest substring
                if is_palindromic and right - left >= max_lps_right - max_lps_left:
                    max_lps_left, max_lps_right = left, right
        return s[max_lps_left : max_lps_right + 1]