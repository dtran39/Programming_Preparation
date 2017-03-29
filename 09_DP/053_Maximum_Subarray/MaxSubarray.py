'''
Problem:
	- Find the contiguous subarray within an array
        (containing at least one number)
            which has the largest sum.
----------------------------------------------------------------------------------------------------
Examples:
    [-2,1,-3,4,-1,2,1,-5,4], -> 6: [4,-1,2,1]
    [-5, -3, -1, -2]        -> -1
    []                      -> null
    [1, 2, 3, 4]            -> 10
    [5, -5,4]               -> 5
----------------------------------------------------------------------------------------------------
Solution:
1. Naive:
    - Try each subarray
    - O(n^2) (leetcode TLE)
2. Recurrence:
    - From maximum sum ends at i, we can find maximum sum ends at i + 1:
        + Since it ends at i + 1, i + 1 is included
        + Decision is whether to elements in the previos, which is made by:
            If it's non-neg, then choose
    - 3 ways: Recursion, recursion with top down memoization, bottom up dp
'''
class Solution(object):
    import sys
    def maxSubArrayBottumUp(self, nums):
        if not nums: return
        maxSumEndingPrev, maxSum = -sys.maxint, -sys.maxint
        for aNum in nums:
            maxSumEndingHere = aNum + (maxSumEndingPrev if maxSumEndingPrev > 0 else 0)
            maxSum = max(maxSum, maxSumEndingHere)
            # Update
            maxSumEndingPrev = maxSumEndingHere
        return maxSum
    def maxSubArrayTopDown(self, nums):
        if not nums: return
        if len(nums) == 1: return nums[0]
        maxSumSubArrayEndAtEach, maxSumSubArray = [nums[0]] * len(nums), nums[0]
        return self.maxSumSubArrayTopDownHelper(nums, 1, maxSumSubArrayEndAtEach, maxSumSubArray)
    def maxSumSubArrayTopDownHelper(self, nums, cur, maxSumSubArrayEndAtEach, maxSumSubArray):
        if cur == len(nums): return maxSumSubArray
        maxSumSubArrayEndAtEach[cur] = nums[cur]
        if maxSumSubArrayEndAtEach[cur - 1] > 0:
            maxSumSubArrayEndAtEach[cur] += maxSumSubArrayEndAtEach[cur - 1]
        maxSumSubArray = max(maxSumSubArray, maxSumSubArrayEndAtEach[cur])
        return self.maxSumSubArrayTopDownHelper(nums, cur + 1, maxSumSubArrayEndAtEach, maxSumSubArray)
    def maxSubArrayRec(self, nums):
        if not nums: return
        if len(nums) == 1: return nums[0]
        return self.maxSumSubArrayRecHelper(nums, 1, nums[0], nums[0])
    def maxSumSubArrayRecHelper(self, nums, cur, maxSumSubArrayEndAtPrev, maxSum):
        # Base case
        if cur == len(nums):
            return maxSum
        # Inductive case
        maxSumSubArrayEndAtCur = nums[cur]
        if maxSumSubArrayEndAtPrev > 0: maxSumSubArrayEndAtCur += maxSumSubArrayEndAtPrev
        return self.maxSumSubArrayRecHelper(nums, cur + 1, maxSumSubArrayEndAtCur,
                                            max(maxSum, maxSumSubArrayEndAtCur))
    def maxSubArrayNaive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return
        maxSubarraySum = -sys.maxint
        for left in range(len(nums)):
            curSum = 0 # starts adding from left
            for right in range(left, len(nums)):
                curSum += nums[right]
                maxSubarraySum = max(maxSubarraySum, curSum)
        return maxSubarraySum
