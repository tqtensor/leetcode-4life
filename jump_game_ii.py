from typing import List


class Solution(object):
    def jump(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 1:
            return 0
        if nums[0] >= len(nums):
            return 1

        dp = [0] * (n)
        dp[-1] = 0
        dp[-2] = 1
        for i in range(n - 2, 0, -1):
            val = nums[i - 1]
            if val >= n - 1 - (i - 1):
                dp[i - 1] = 1  # can jump directly to the end index
            elif val == 0:
                dp[i - 1] = float("inf")  # cannot jump to any node
            else:
                dp[i - 1] = min(dp[i : i + val]) + 1
        return dp[0]
