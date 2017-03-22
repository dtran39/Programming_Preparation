'''
Problem:
    -

----------------------------------------------------------------------------------------------------
Examples: 

----------------------------------------------------------------------------------------------------
Solution:
1. Brute force
2. Use Division
    - Get the product of all elements in array called totalProduct
    - Loop through each element: products[i] = totalProduct / nums[i]
    - Special case: contains a 0
        + only the index with 0 will have value that different from 0
3. Use left and right array
    - Extra space
4. Two pass: left and right
    - Pass 1 from 1 to n: (right)
        + outpus[0] = 1
        + outputs[i] = outputs[i - 1] * nums[i - 1]
    - Pass 2: from n - 1 to 0 (left)
        + keep track of the products of all elements in the right, called productRight
        + productRight *= nums[i + 1]
        + outputs[i] *= productright
'''
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        output = [1] * n
        prod_left = 1
        # Left
        for i in range(1, n):
            prod_left *= nums[i - 1]
            output[i] = prod_left
        # Right
        prod_right = 1
        for i in range(n - 2, -1, -1):
            prod_right *= nums[i + 1]
            output[i] *= prod_right
        return output
        