from typing import List


class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:

        width = len(grid[0])
        height = len(grid)

        dp = [[(0, 0)] * width for _ in range(height)]

        max_len = 0
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 0:
                    dp[i][j] == (0, 0)
                else:
                    if max_len == 0:
                        max_len = 1

                    if i == 0 and j == 0:
                        dp[i][j] = (1, 1)
                    elif i == 0:
                        dp[i][j] = (1, dp[i][j - 1][1] + 1)  # first row
                    elif j == 0:
                        dp[i][j] = (dp[i - 1][j][0] + 1, 1)  # first column
                    else:
                        dp[i][j] = (
                            dp[i - 1][j][0] + 1,
                            dp[i][j - 1][1] + 1,
                        )  # row and column incremental count
                        for k in range(
                            max_len, min(dp[i][j])
                        ):  # k+1 is side length of the square
                            if dp[i - k][j][1] >= k + 1 and dp[i][j - k][0] >= k + 1:
                                max_len = k + 1
        # print(dp)
        return max_len * max_len


if __name__ == "__main__":
    Solution.largest1BorderedSquare(object, grid=[[1, 1, 1], [1, 0, 1], [1, 1, 1]])
