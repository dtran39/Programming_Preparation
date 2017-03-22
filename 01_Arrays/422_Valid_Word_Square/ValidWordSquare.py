'''
Problem:
	- Given a sequence of words, check whether it forms a valid word square.

	A sequence of words forms a valid word square if the kth row and column read the exact same string, 
		where 0 ≤ k < max(numRows, numColumns).

----------------------------------------------------------------------------------------------------
Examples: 
Input:
[
  "abcd",
  "bnrt",
  "crmy",
  "dtye"
]

Output:
true

Input:
[
  "abcd",
  "bnrt",
  "crm",
  "dt"
]

Output:
true

Input:
[
  "ball",
  "area",
  "read",
  "lady"
]

Output:
false

----------------------------------------------------------------------------------------------------
Solution: 
	Swap index
'''
class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        # Fill zeroes
        max_len = len(words[0])
        if len(words) != max_len:
            return False
        for i in range(len(words)):
            cur_word = words[i]
            if len(cur_word) > max_len:
                return False
            if len(cur_word) < max_len:
                words[i] = cur_word + " " * (max_len - len(cur_word))
        # Loop
        for r in range(max_len):
            for c in range(max_len):
                if words[r][c] != words[c][r]:
                    return False
        return True
    def validWordSquare(self, words):
        for i in range(len(words)):
            for j in range(len(words[i])):
                if j >= len(words) or i >= len(words[j]) or words[i][j] != words[j][i]:
                    return False
        return True