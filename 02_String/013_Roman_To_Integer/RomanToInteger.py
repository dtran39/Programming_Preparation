class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Special case
        if not s: return 0
        roman_num_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        numeral_val = 0
        for i in range(len(s)):
            cur_val, next_val = roman_num_dict[s[i]], 0
            if i < len(s) - 1: next_val = roman_num_dict[s[i + 1]]
            # If the latter chr bigger than current chr: then must add (latter - current). Else: add current
            if cur_val >= next_val:
                numeral_val += cur_val
            else:
                numeral_val -= cur_val
        return numeral_val
sol = Solution()
print sol.romanToInt('XIV')
print sol.romanToInt('DCXXI')
print sol.romanToInt('DCXXVIII')
print sol.romanToInt('CDXII')