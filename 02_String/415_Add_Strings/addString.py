'''
Problem:
	-
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
Note:
	The length of both num1 and num2 is < 5100.
	Both num1 and num2 contains only digits 0-9.
	Both num1 and num2 does not contain any leading zero.
	You must not use any built-in BigInteger library or convert the inputs to integer directly.
----------------------------------------------------------------------------------------------------
Examples: 
----------------------------------------------------------------------------------------------------
Solution: 
    Solution 1: 
    	starts from the bottom
    	can convert to chr list for easier handle
    	Notice:
    		Loop backward (from big_len - 1 to 0)
    		Check if should add small_digit: if big_len - i - 1 < small_len
    			add small_num[i - digit_diff]
    Solution 2: two pointers starts from the bottom
        More elegant
'''
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        big_num, small_num = num1, num2
        big_len, small_len = len(num1), len(num2)
        # assign as, big num, small num, swap if necessary
        if small_len > big_len:
            big_num, small_num, big_len, small_len = num2, num1, small_len, big_len
        digit_diff = big_len - small_len
        # Work backward
        digit_arr = [' '] * big_len
        carry = 0
        for i in range(big_len - 1, -1, -1):
            # get sum of digits
            sum_digits = int(big_num[i]) + carry
            if big_len - i <= small_len:
                print i
                sum_digits += int(small_num[i - digit_diff])
            # push into results, update carry
            digit_arr[i] = str(sum_digits % 10)
            carry = sum_digits / 10
        # converted back to string, add carry if needed
        new_num = ''.join(digit_arr)
        if carry > 0:
            new_num = str(carry) + new_num
        return new_num
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = []
        i, j, carry = len(num1) - 1, len(num2) - 1, 0
        
        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += ord(num1[i]) - ord('0');
                i -= 1
            if j >= 0:
                carry += ord(num2[j]) - ord('0');
                j -= 1
            result.append(str(carry % 10))
            carry /= 10
        result.reverse()

        return "".join(result)
