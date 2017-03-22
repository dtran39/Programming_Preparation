'''
Problem:
    Implement a basic calculator to evaluate a simple expression string.
    The expression string contains only non-negative integers, +, -, *, / operators and empty spaces.
        The integer division should truncate toward zero.
    You may assume that the given expression is always valid.

----------------------------------------------------------------------------------------------------
Examples:
"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5
"3 * 4 * 5 - 72 / 8 * 3 + 1" = 60 - 27 + 1 = 34
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
    - Just based on priority: () > *, / > +, -
        + see (: must clean everything until see )
        + *, /: push to stack
        + +, -: must clean all * and /
Cleaning:
    - CalculateOnce function: passing two stacks along with value,
        since operations usually on the stack
'''
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        def calculateOnce(val1, val2, operator):
            if operator == '+': return val1 + val2
            if operator == '-': return val1 - val2
            if operator == '*': return val1 * val2
            if operator == '/': return val1 / val2
            return val1 + val2
        def calculateOnceUpdateStack(operand_s, operator_s):
            operand_s.append(calculateOnce(operand_s.pop(), operand_s.pop(), operator_s.pop()))
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
            elif s[i] in ['*', '/', ')']: operator_s.append(s[i])
            elif s[i] == '(':
                while operator_s[-1] != ')':
                    calculateOnceUpdateStack(operand_s, operator_s)
                operator_s.pop() # pop the ')'
            elif s[i] in ['+', '-']:
                while operator_s and operator_s[-1] in ['*', '/']:
                    calculateOnceUpdateStack(operand_s, operator_s)
                operator_s.append(s[i])
            i -= 1
        while operator_s:
            calculateOnceUpdateStack(operand_s, operator_s)
        return operand_s.pop()
sol = Solution()
print sol.calculate("") #0
print sol.calculate("3+2*2")
print sol.calculate("((3 * 2) + 2) / 3") #2
