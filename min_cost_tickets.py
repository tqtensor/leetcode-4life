from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [0 for _ in range(n + 1)]
        # pointer to the index in days array, which is 7 days before the current day
        seven = 0
        # pointer to the index in days array, which is 30 days before the current day
        thirty = 0

        for i in range(n):
            while days[i] > days[seven] + 6:  # update the 7 day pointer
                seven += 1
            while days[i] > days[thirty] + 29:  # update the 30 day pointer
                thirty += 1
            # Take the minimum cost at a given day
            dp[i + 1] = min(
                dp[i] + costs[0], dp[seven] + costs[1], dp[thirty] + costs[2]
            )

        return dp[-1]


if __name__ == "__main__":
    solution = Solution()
    solution.mincostTickets(days=[1, 4, 6, 7, 8, 20, 55], costs=[2, 7, 15])
