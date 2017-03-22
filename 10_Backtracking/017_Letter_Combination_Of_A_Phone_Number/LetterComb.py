'''
Problem:
    -

----------------------------------------------------------------------------------------------------
Examples: 

----------------------------------------------------------------------------------------------------
Solution: 
1. Backtracking
2. DFS
'''
class Solution(object):
    def letterCombinationsRec(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        val_of_nums = [" ", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        if not digits: return []
        combs = self.letterCombinationsRec(digits, 0, [""], val_of_nums)
        return combs
    def letterCombinationsRec(self, digits, curDigit, cur_combs, val_of_nums):
        if curDigit == len(digits): return cur_combs
        new_combs = []
        for a_comb in cur_combs:
            possible_chrs = val_of_nums[int(digits[curDigit])]
            for new_chr in possible_chrs:
                new_combs.append(a_comb + new_chr)
        return self.letterCombinationsRec(digits, curDigit + 1, new_combs, val_of_nums)
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # DP ways
        # Invalid case
        if not digits: return []
        # Base case
        chrs_lists = [" ", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        cur_combs = [""]
        for a_digit in digits:
            # For each additional digit, generate new combinations 
                # from characters made from that current digit and the old combinations
            new_combs = []
            chrs_list = chrs_lists[int(a_digit)]
            for a_comb in cur_combs:
                for a_chr in chrs_list:
                    new_combs.append(a_comb + a_chr)
            cur_combs = new_combs
        return cur_combs