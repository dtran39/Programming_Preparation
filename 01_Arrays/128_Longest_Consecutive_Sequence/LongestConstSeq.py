'''
Problem:
	-
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
----------------------------------------------------------------------------------------------------
Examples: 
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.
----------------------------------------------------------------------------------------------------
Solution: Union find
	- First find the chain
	- Then expand the finding to left and right
'''
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_lcs = 0
        value_to_its_lcs = {}
        for num in nums:
        	if num not in value_to_its_lcs:
        		left_lcs, right_lcs = 0, 0
        		if num - 1 in value_to_its_lcs: 
        			left_lcs = value_to_its_lcs[num - 1]
        		if num + 1 in value_to_its_lcs:
        			right_lcs = value_to_its_lcs[num + 1]
        		# Put current value lcs: left + right + 1 (itself)
        		cur_lcs = left_lcs + right_lcs + 1
        		max_lcs = max(max_lcs, cur_lcs)
        		value_to_its_lcs[num] = cur_lcs
        		value_to_its_lcs[num - left_lcs] = cur_lcs        		
        		value_to_its_lcs[num + right_lcs] = cur_lcs        		        		
        return max_lcs

        