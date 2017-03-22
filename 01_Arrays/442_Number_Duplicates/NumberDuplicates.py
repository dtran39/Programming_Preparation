'''
Problem:
		Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

		Find all the elements that appear twice in this array.

		Could you do it without extra space and in O(n) runtime?
	-
----------------------------------------------------------------------------------------------------
Examples: 
	[4,3,2,7,8,2,3,1]			[2,3]
----------------------------------------------------------------------------------------------------
Solution: 
Solution 1: add n + 1
    - Can generalize to find all types of frequency (not just 0)
Solution 2: -(abs(nums[i])), if already negative: add to result
    - Easy to deal with overflow
'''
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Store frequency of each element
        n = len(nums)
        for i in range(n):
            # Remember to mod by (n + 1), because (the value in array is being modified)
            nums[(nums[i] % (n + 1)) - 1] += (n + 1)
        # Get frequency of each element
        dissappeared = []
        for i in range(n):
            if nums[i] / (n + 1) == 2:
                dissappeared.append(i + 1)
        return dissappeared
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for x in nums:
            if nums[abs(x)-1] < 0:
                res.append(abs(x))
            else:
                nums[abs(x)-1] *= -1
        return res