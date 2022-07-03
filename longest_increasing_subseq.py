from bisect import bisect_left
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            # Here we pass three arg's, which means find the position
            # of nums[i] in the nums array within index i.
            idx = bisect_left(nums, nums[i], hi=i)
            if idx != i:
                nums[idx], nums[i] = nums[i], float("inf")
        return nums.index(float("inf")) if float("inf") in nums else n


if __name__ == "__main__":
    Solution.lengthOfLIS(object, nums=[10, 9, 2, 5, 3, 7, 101, 18])
