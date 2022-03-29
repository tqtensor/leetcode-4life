import math


class Solution:
    def numSquares(self, n: int) -> int:
        if math.ceil(n**0.5) == math.floor(n**0.5):
            return 1
        dp = [i for i in range(n + 1)]
        for i in range(1, math.ceil(n**0.5) + 1):
            sqi = i**2
            for j in range(sqi, n + 1):
                dp[j] = min(dp[j], 1 + dp[j - sqi])

        return dp[n]


if __name__ == "__main__":
    Solution.numSquares(object, n=10)
