'''
Problem:
    - Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
----------------------------------------------------------------------------------------------------
Examples: 
    [4,3,2,7,8,2,3,1]                   [5,6]
----------------------------------------------------------------------------------------------------
Solution: 
Solution 1: add n + 1
    - Can generalize to find all types of frequency (not just 0)
Solution 2: -(abs(nums[i]))
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
            if nums[i] / (n + 1) == 0:
                dissappeared.append(i + 1)
        return dissappeared
        
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # For each number i in nums,
        # we mark the number that i points as negative.
        # Then we filter the list, get all the indexes
        # who points to a positive number
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = - abs(nums[index])

        return [i + 1 for i in range(len(nums)) if nums[i] > 0]
