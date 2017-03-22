'''
Problem:
	- Implement a basic calculator to evaluate a simple expression string.
    The expression string may contain open ( and closing parentheses ),
        the plus + or minus sign -, non-negative integers and empty spaces .
    You may assume that the given expression is always valid.

----------------------------------------------------------------------------------------------------
Examples:
"1 + 1" = 2
" 2-1 + 2 " = 3
"(1+(4+5+2)-3)+(6+8)" = 23
----------------------------------------------------------------------------------------------------
Solution:
    - Dijkstra's two stack algorithms: one for operands, one for operators
Things to consider:
    - Must calculate from left to right, or you will get a different result:
        for ex: (3 - 5 + 7) if calculate from right to left would be 3 - (5 + 7) = -9
        One solution: traverse string in backward order
    - Must take care of multiple digits number
		+ When finish traversing, remember to move pointer back once
			(since ptr will be to the right once)
    - Trick: to check if all computation has been executed, check if operator stack is empty
	- Parentheses: must be handle immediately:
'''

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        def calculateOnce(val1, val2, operator):
            return val1 + (val2 if operator == '+' else -val2)
        if not s: return 0
        operand_s, operator_s = [], []
        i = len(s) - 1
        while i >= 0:
            # Traverse to get number
            if s[i].isdigit():
                num, dec_ptr = 0, 1
                while i >= 0 and s[i].isdigit():
                    num += dec_ptr * (ord(s[i]) - ord('0'))
                    i -= 1
                    dec_ptr *= 10
                operand_s.append(num)
                i += 1
            elif s[i] in ['+', '-', ')']: operator_s.append(s[i])
            elif s[i] == '(':
                while True:
                    operator = operator_s.pop()
                    if operator == ')': break
                    else:
                        val1, val2 = operand_s.pop(), operand_s.pop()
                        operand_s.append(calculateOnce(val1, val2, operator))
            i -= 1
        while operator_s:
            val1, val2, operator = operand_s.pop(), operand_s.pop(), operator_s.pop()
            operand_s.append(calculateOnce(val1, val2, operator))
        return operand_s.pop()
sol = Solution()
# print sol.calculate("") #0
# print sol.calculate("13 + 10 - (40 + 30)")# -47
# print sol.calculate("1 + 1")# 2
# print sol.calculate(" 2-1 + 2 ")# 3
# print sol.calculate("1 + (4 + 5 + 2) - 3")# 9
# print sol.calculate("(1+(4+5+2)-3)+(6+8)") #23
