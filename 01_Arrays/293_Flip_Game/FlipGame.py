'''
Problem:
    -
You are playing the following Flip Game with your friend:
    Given a string that contains only these two characters: + and -, 
    you and your friend take turns to flip two consecutive "++" into "--". 
    The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to compute all possible states of the string after one valid move.

----------------------------------------------------------------------------------------------------
Examples: 
For example, given s = "++++", after one move, it may become one of the following states:

[
  "--++",
  "+--+",
  "++--"
]
If there is no valid move, return an empty list [].
----------------------------------------------------------------------------------------------------
Solution: 
    Go through every character: if s[i] and s[i + 1] == "++", replace with -- and add to resultsw 
'''
class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        for i in range(len(s) - 1):
            if s[i] == "+" and s[i + 1] == "+":
                new_str = ""
                if i > 0:
                    new_str += s[: i]
                new_str += "--"
                if i < len(s) - 2:
                    new_str += s[i + 2 : len(s)] 
                result.append(new_str)
        return result