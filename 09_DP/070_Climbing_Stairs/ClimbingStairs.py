class Solution(object):
    def climbStairs(self, n):
        from math import sqrt, pow
        Phi, phi = (1 + sqrt(5)) / 2, (1 - sqrt(5)) / 2
        return int((pow(Phi, n + 1) - pow(phi, n + 1)) / sqrt(5))
    def climbStairsBottomUp(self, n):
        if n < 2: return 1
        waysToClimbToPrev, waysToClimbToPrevPrev = 1, 1
        for i in range(2, n + 1):
            waysToClimbToCur = waysToClimbToPrevPrev + waysToClimbToPrev
            waysToClimbToPrevPrev = waysToClimbToPrev
            waysToClimbToPrev = waysToClimbToCur
        return waysToClimbToPrev
    def climbStairsTopDown(self, n):
        return self.climbStairsTopDownRec(n, [1, 1])
    def climbStairsTopDownRec(self, n, memo):
        if len(memo) >= n + 1:
            return memo[n]
        result = self.climbStairsTopDownRec(n - 1, memo) + self.climbStairsTopDownRec(n - 2, memo)
        memo.append(result)
        return result
    def climbStairsRec(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2: return 1
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
