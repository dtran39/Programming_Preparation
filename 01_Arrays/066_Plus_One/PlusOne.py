'''
Problem:
	- Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

	You may assume the integer do not contain any leading zero, except the number 0 itself.

	The digits are stored such that the most significant digit is at the head of the list.

----------------------------------------------------------------------------------------------------
Examples: 

----------------------------------------------------------------------------------------------------
Solution: 
	Add from the end, store a carry
	If have extra carry, add the carry
'''
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 0
        for i in range(len(digits) - 1, -1, -1):
        	new_num = digits[i] + carry
        	if i == len(digits) - 1: new_num += 1
        	new_digit = new_num % 10
        	carry = new_num / 10
        	digits[i] = new_digit
        	if carry == 0:
        		return digits
        if carry > 0: digits = [carry] + digits
        return digits
        
        