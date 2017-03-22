'''
Problem:
	- Given an array nums,
        there is a sliding window of size k
        which is moving from the very left of the array to the very right.
        You can only see the k numbers in the window.
        Each time the sliding window moves right by one position.

----------------------------------------------------------------------------------------------------
Examples: nums = [1,3,-1,-3,5,3,6,7], and k = 3.
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 output: [3,3,5,5,6,7].
----------------------------------------------------------------------------------------------------
Solution:
    + A descendingly sorted window, which keeps only potential candidate for window maxes
    + When looping through a new element,
        discard all elements in the window that is smaller than new element
            To maintain descendingly sort in the queue
        -> Will discard all if the element is the biggest
    + Then add the left most element (which is the max) to the window maxes output:
        + Only do it from i == k - 1 (when the window is full size)
        + Also, must check if the left most is still in window range
            Check if the index is > i - k
            Since we check it every time we meet a new element
                We only need to check the left most, because the one after that will be sure in range
    + Also the window is guaranteed always at least have the new element
        And the new element is guaranteed to be in range
        Therefore each time after i == k - 1 we will have a value to add on the window maxes
'''
from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        indicesWindowSortedDescByValue = deque()
        window_maxes = []
        for i in xrange(len(nums)):
            # before adding i,
                #remove any idx in queue (to the left of i) has smaller values
            while indicesWindowSortedDescByValue and nums[indicesWindowSortedDescByValue[-1]] < nums[i]:
                indicesWindowSortedDescByValue.pop()
            indicesWindowSortedDescByValue.append(i)
            # chekc the max value (which is also left most) if it is out of window range
            if indicesWindowSortedDescByValue[0] <= i - k:
                indicesWindowSortedDescByValue.popleft()
            # adding the max value (which is also left most)
                #only when the window is full size: i >= k - 1 (since i starts from 0)
            if i >= k - 1:
                window_maxes.append(nums[indicesWindowSortedDescByValue[0]])
        return window_maxes
