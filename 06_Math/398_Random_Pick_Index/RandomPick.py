'''
Problem:
	- Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.
Note:
The array size can be very large. Solution that uses too much extra space will not pass the judge.

----------------------------------------------------------------------------------------------------
Examples: 

----------------------------------------------------------------------------------------------------
Solution: 
1. O(n) space: maintain a map from value to array of indices
2. O(n) time:
	randomly select an int from 0 to the nums of target. 
	If x equals 0, set the res as the current index. 
	The probability is always 1/nums for the latest appeared number. 
	For example, 1 for 1st num, 1/2 for 2nd num, 1/3 for 3nd num (1/2 * 2/3 for each of the first 2 nums).
'''
class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums
    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        import random
        result, count = None, 0
        # Use count
        for i in range(len(self.nums)):
            if self.nums[i] != target: continue
            count += 1
            if random.randint(0, count - 1) == 0:
                result = i
        return result

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)