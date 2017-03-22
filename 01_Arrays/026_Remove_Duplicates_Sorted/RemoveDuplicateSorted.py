'''
Problem:
	- Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

----------------------------------------------------------------------------------------------------
Examples: 
For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.

Show Company Tags
Show Tags
Show Similar Problems

----------------------------------------------------------------------------------------------------
Solution: 
	- Two pointers:
	- Time: O(n), space: O(1)
'''
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Edge cases
        if not nums: return 0
        n, next_pos = len(nums), 1
        if n == 1: return 1
        # Loop
        for i in xrange(1, n):
        	# If find a different element with next_pos - 1, put in the next available position
        		# How:  swap nums[i] with nums[next_pos]
        	if nums[i] != nums[next_pos - 1]:
        		temp = nums[i]
        		nums[i] = nums[next_pos]
        		nums[next_pos] = temp
        		next_pos += 1
        return next_pos
