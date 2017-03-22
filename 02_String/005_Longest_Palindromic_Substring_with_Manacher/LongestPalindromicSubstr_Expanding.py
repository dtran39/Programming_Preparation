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
    Expanding from center:
        We observe that a palindrome mirrors around its center. 
            Therefore, a palindrome can be expanded from its center, and there are only 2N-1 such centers.       
        2n - 1 because the center of a palindrome can be in between two letters. 
            Such palindromes have even number of letters (such as “abba”) and its center are between the two ‘b’s.
    Caution:
        Remember to move back left and right counter for one step (off by one)

    Time: O(n ^ 2), space: O(1)
'''
# http://leetcode.com/2011/11/longest-palindromic-substring-part-ii.html
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Edge case
        if not s: return ""
        # Normal case: Initialization
        s_len, max_lps_left, max_lps_right = len(s), 0, 0
        # Go through each starting point
        for i in range(s_len):
            # Even case: expanding from the gap between i and i + 1
            left, right = i, i + 1
            while left >= 0 and right < s_len and s[left] == s[right]:
                left, right = left - 1, right + 1
            left, right = left + 1, right - 1
            # Update if find new longest palindromic substring
            if right - left >= max_lps_right - max_lps_left:
                max_lps_left, max_lps_right = left, right
            # Odd case: expanding from i
            left, right = i, i
            while left >= 0 and right < s_len and s[left] == s[right]:
                left, right = left - 1, right + 1
            # Update if find new longest palindromic substring
            left, right = left + 1, right - 1            
            if right - left >= max_lps_right - max_lps_left:
                max_lps_left, max_lps_right = left, right
        return s[max_lps_left : max_lps_right + 1]