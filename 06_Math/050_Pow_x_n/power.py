'''
Problem:
	-

----------------------------------------------------------------------------------------------------
Examples: 

----------------------------------------------------------------------------------------------------
Solution: 
1. Linear
2. Divide and conquer: log
'''
class Solution(object):
    def myPowLinear(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        prod = 1
        for i in range(n):
            prod *= x
        return prod
	def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # Base case
        if n == 0: return 1
        # Negative case
        if n < 0:
            n = -n
            x = 1 / x
        # If n is odd, must multiply with x
        result = pow(x * x, n / 2)
        if n % 2 == 1: result *= x
        return result
	def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # Base case
        if n == 0: return 1
        # Negative case
        if n < 0:
            n = -n
            x = 1 / x
        # If n is odd, must multiply with x
        result = 1
        while n > 0:
            if n % 2 == 1: result *= x
            x *= x
            n >>= 1
        return result