'''
Problem:
    - Given a non-empty array of integers, return the third maximum number in this array. 
        If it does not exist, return the maximum number. The time complexity must be in O(n).
----------------------------------------------------------------------------------------------------
Examples: 
Example 1:      Input: [3, 2, 1]        Output: 1
    Explanation: The third maximum is 1.
Example 2:      Input: [1, 2]           Output: 2
    Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:      Input: [2, 2, 3, 1]     Output: 1
    Explanation: Note that the third maximum here means the third maximum distinct number.
    Both numbers with value 2 are both considered as second maximum.
----------------------------------------------------------------------------------------------------
Solution: 
3 space to store three maximums:
    Update when looping through each element
Solution 1: Update and push
Solution 2: Remove the third max index, add new in, then sort
'''
class Solution(object):
    def thirdMax(self, nums):
        import sys
        """
        :type nums: List[int]
        :rtype: int
        """
        maxes = [-sys.maxint] * 3
        for a_num in nums:
            if a_num > maxes[0]:
                maxes[2] = maxes[1]
                maxes[1] = maxes[0]
                maxes[0] = a_num
            elif a_num < maxes[0] and a_num > maxes[1]:
                maxes[2] = maxes[1]
                maxes[1] = a_num
            elif a_num < maxes[1] and a_num > maxes[2]:
                maxes[2] = a_num
        if maxes[2] == -sys.maxint:
            return maxes[0]
        return maxes[2]
    def thirdMax(self, nums):
        max_array = [-sys.maxint] * 3
        for num in nums:
            if num > max_array[0] and num not in max_array:
                max_array = [num, max_array[1], max_array[2]]
                max_array.sort()
                third_max = max_array[0]
        if max_array[0] == -sys.maxint:
            return max_array[2]
        return third_max