'''
Problem:
    - Shuffle a set of numbers without duplicates.
----------------------------------------------------------------------------------------------------
Examples: 
// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();
----------------------------------------------------------------------------------------------------
Solution: 
    for i in range(n)
        Generate a random numbers
        swap nums[i] with nums[random_num]
'''
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        new_nums = self.nums[:]
        n = len(new_nums)
        import random
        for i in range(n):
            rand_num = random.randint(0, n - 1)
            # Swap nums[i] with nums[randint]
            temp = new_nums[i]
            new_nums[i] = new_nums[rand_num]
            new_nums[rand_num] = temp
        return new_nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()