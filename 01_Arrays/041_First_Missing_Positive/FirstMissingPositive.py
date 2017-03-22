'''
Problem:
	- Given an unsorted integer array, find the first missing positive integer.

----------------------------------------------------------------------------------------------------
Examples: 
# Given [1,2,0] return 3,
# and [3,4,-1,1] return 2.
	[3, 4, -1, 1] 			[-1, 4, 3, 1] 		[-1, 1, 3, 4]

----------------------------------------------------------------------------------------------------
Solution: 
	- Based on the fact that an array of length n can only contains positive integer from 1 to n
	- Therefore: just use the array itself as a map: store value i in array[i - 1]
	- Then go through the array again, check to see if arr[i] != i + 1
	- If cannot find anything, the next missing integer is n + 1
	Caution: must only do swap if number is not in its position, 
		or we will have infinite loop (try to swap a number with itself)
	Time: O(n), space: O(1)
'''
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 1
        n = len(nums)
        i = 0
        while i < n:
        	a_num = nums[i]
        	# Swap nums[a_num] and nums[i]
        	if a_num > 0 and a_num - 1 < n and a_num != nums[a_num - 1]:
        		nums[i] = nums[a_num - 1]
        		nums[a_num - 1] = a_num
        	else:
        	    i += 1
        # Go through array again, check the first missing
        print nums
        for i in range(n):
        	if nums[i] != i + 1:
        		return i + 1
        return n + 1        		