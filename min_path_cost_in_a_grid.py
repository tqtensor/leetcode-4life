from typing import List


class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dp = [[float("inf") for _ in range(n)] for _ in range(m)]
        dp[-1] = grid[-1]

        for i in reversed(range(m - 1)):
            for j in reversed(range(n)):

                for k in range(n):
                    dp[i][j] = min(
                        dp[i][j], grid[i][j] + moveCost[grid[i][j]][k] + dp[i + 1][k]
                    )
        return min(dp[0])


if __name__ == "__main__":
    Solution().minPathCost(
        grid=[[5, 3], [4, 0], [2, 1]],
        moveCost=[[9, 8], [1, 5], [10, 12], [18, 6], [2, 4], [14, 3]],
    )
