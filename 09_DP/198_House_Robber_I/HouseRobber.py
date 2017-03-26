class Solution(object):
    def robBottomUp(self, nums):
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        maxRobbedAtPrevPrev, maxRobbedAtPrev = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            maxRobbedAtCur = max(maxRobbedAtPrev, maxRobbedAtPrevPrev + nums[i])
            maxRobbedAtPrevPrev = maxRobbedAtPrev
            maxRobbedAtPrev = maxRobbedAtCur
        return maxRobbedAtPrev
    def robTopDown(self, nums):
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        maxRobbedAtEach = [nums[0], max(nums[0], nums[1])] + [-1] * (len(nums) - 2)
        return self.robTopDownHelper(nums, len(nums) - 1, maxRobbedAtEach)
    def robTopDownHelper(self, nums, end, maxRobbedAtEach):
        if maxRobbedAtEach[end] != -1:
            return maxRobbedAtEach[end]
        maxRobbedAtEnd = max(self.robTopDownHelper(nums, end - 1, maxRobbedAtEach),
                            self.robTopDownHelper(nums, end - 2, maxRobbedAtEach) + nums[end])
        maxRobbedAtEach[end] = maxRobbedAtEnd
        return maxRobbedAtEnd
    def robRec(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        return self.robRecHelper(nums,  len(nums) - 1)
    def robRecHelper(self, nums, end):
        if end == 0: return nums[end]
        if end == 1: return max(nums[0], nums[end])
        return max(self.robRecHelper(nums,  end - 1),
                        self.robRecHelper(nums, end - 2) + nums[end])
