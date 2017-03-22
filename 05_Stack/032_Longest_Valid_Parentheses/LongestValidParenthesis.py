'''
Problem:
	- Given a string containing just the characters '(' and ')', 
	- find the length of the longest valid (well-formed) parentheses substring.
----------------------------------------------------------------------------------------------------
Examples: 
	- For "(()", the longest valid parentheses substring is "()", which has length = 2.
	- Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
----------------------------------------------------------------------------------------------------
Solution: 
1. Simple approach: Check all substring:
	+ O(n^3): O(n^2) substring, O(n) to Check
2. More efficient approach:
	+  For every string, check if it is a valid string or not. 
	+ If valid and length is more than maximum length so far, then update maximum length
	+ Use stack
	+ O(n^2)
3. Efficient: 
	 store indexes of previous starting brackets in a stack. 
	 The first element of stack is 
	 	a special element that provides index before beginning of valid substring (base for next valid string).
'''