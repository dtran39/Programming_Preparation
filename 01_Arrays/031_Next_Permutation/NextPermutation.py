'''
Problem:
	-
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.
----------------------------------------------------------------------------------------------------
Examples: 
1,2,3 → 1,3,2
1,1,5 → 1,5,1
2,3,1 -> 3, 1, 2
3,2,1 → 1,2,3
3, 2, 8, 4, 1 -> 3, 4, 1, 2, 8
----------------------------------------------------------------------------------------------------
Solution: 
	- Observation: 3 > 2 -> 3 is up front (same with 5 and 1)
	- Scanning from the right
		1. find a digit not in the ascending order from the right 
			(meaning find i such that nums[i] <= nums[i + 1])
		Edge case: all digits are in ascending order (loop until the beginning of the array):
			Return array reverse
		2. Then find digit j in the right of i (j > i) such that nums[j] is the smallest number > nums[i]
		3. Swap i and j
		4. sort from right of i original position
	- Time: O(nlogn), space: O(n)
'''
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 1: return
        i = len(nums) - 2
       	while i > -1:
       		# Loop until find a digit smaller than its right
       		if nums[i] < nums[i + 1]:
       			break
       		i -= 1
       	# If cannot found, return the reverse
       	if i == -1: return nums.reverse()
       	# find the smallest number on the right side that is greater than nums[i]
       	smallest_idx = i + 1
       	for j in range(i + 1, len(nums)):
       		if nums[j] > nums[i] and nums[j] < nums[smallest_idx]:
       			smallest_idx = j
       	# swap
       	temp = nums[i]
       	nums[i] = nums[smallest_idx]
       	nums[smallest_idx] = temp
       	# sort
       	nums[i + 1:] = sorted(nums[i + 1:])
