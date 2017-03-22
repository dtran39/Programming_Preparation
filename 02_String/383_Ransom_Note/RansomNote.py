'''
Problem:
    -
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.


----------------------------------------------------------------------------------------------------
Examples: 
    canConstruct("a", "b") -> false
    canConstruct("aa", "ab") -> false
    canConstruct("aa", "aab") -> true
----------------------------------------------------------------------------------------------------
Solution: 
    Time: O(n), space: O(1) because only lowercase letter
'''
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransom_chrs_needed = [0] * 26
        num_ransom_chrs_needed = 0
        # Get list of characters needed for ransom
        for a_chr in ransomNote:
            chr_val = ord(a_chr) - ord('a')
            ransom_chrs_needed[chr_val] += 1
            num_ransom_chrs_needed += 1
        # Go through magazine, check off each character needed for ransom
        for a_chr in magazine:
            chr_val = ord(a_chr) - ord('a')
            if ransom_chrs_needed[chr_val] > 0:
                ransom_chrs_needed[chr_val] -= 1
                num_ransom_chrs_needed -= 1
                if num_ransom_chrs_needed == 0:
                    return True
        # If loop through the whole magazine and hasn't got all characters checked off, return False
        return not num_ransom_chrs_needed
        