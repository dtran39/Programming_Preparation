'''
Problem:
	- Say you have an array for which
        the ith element is the price of a given stock on day i.
    - If you were only permitted to complete at most one transaction
        (ie, buy one and sell one share of the stock),
            design an algorithm to find the maximum profit.
----------------------------------------------------------------------------------------------------
Examples:
Input: [7, 1, 5, 3, 6, 4]               Output: 5  max. difference = 6-1 = 5
    (not 7-1 = 6, as selling price needs to be larger than buying price)
Input: [7, 6, 4, 3, 1]                  Output: 0
    In this case, no transaction is done, i.e. max profit = 0.
----------------------------------------------------------------------------------------------------
Solution:
1. Convert to problem:
    find the pair of elements that has biggest difference (or zero if differences are negative)
2. Solution: keep track of the min and the largest diff
    + Update min
    + Update largest diff, which is equal arr[i] - min
'''
class Solution(object):
    import sys
    def maxProfitBottomUp(self, prices):
        minPrice, maxProfit = sys.maxint, 0
        for curPrice in prices:
            minPrice = min(minPrice, curPrice)
            maxProfit = max(maxProfit, curPrice - minPrice)
        return maxProfit
    def maxProfitTopDown(self, prices):
        if not prices or len(prices) == 1: return 0
        minAtEachEnd, maxDiffAtEachEnd  = [-1] * len(prices), [-1] * len(prices)
        minAtEachEnd[0] = prices[0]
        maxDiffAtEachEnd[0] =  0
        return self.maxProfitTopDownHelper(prices, minAtEachEnd, maxDiffAtEachEnd, 1)
    def maxProfitTopDownHelper(self, prices, minAtEachEnd, maxDiffAtEachEnd, cur):
        if cur == len(prices): return maxDiffAtEachEnd[-1]
        minAtEachEnd[cur] = min(minAtEachEnd[cur - 1], prices[cur])
        maxDiffAtEachEnd[cur] = max(maxDiffAtEachEnd[cur - 1], prices[cur] - minAtEachEnd[cur])
        return self.maxProfitTopDownHelper( prices, minAtEachEnd, maxDiffAtEachEnd, cur + 1)
    def maxProfitRec(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) == 1: return 0
        return self.maxProfitRecHelper(prices, prices[0], prices[1] - prices[0], 1)
    def maxProfitRecHelper(self, prices, minPrice, maxDiff, cur):
        # Base case
        if cur == len(prices): return max(maxDiff, 0)
        # Inductive case
        newMinPrice = min(minPrice, prices[cur])
        newMaxDiff = max(maxDiff, prices[cur] - newMinPrice)
        return self.maxProfitRecHelper(prices, newMinPrice, newMaxDiff, cur + 1)
sol = Solution()
