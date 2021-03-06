from typing import List


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        i, j = 0, len(nums) - 1

        res = 0
        NUM = 10**9 + 7
        while i <= j:
            if nums[i] + nums[j] > target:
                j -= 1
            elif nums[i] + nums[j] <= target:
                # For each position inside the range (i, j),
                # we have two choices to select or not select
                # an element, so 2**n possibilities
                res += pow(2, j - i, NUM)
                i += 1
        return res % NUM


if __name__ == "__main__":
    Solution.numSubseq(object, nums=[3, 5, 6, 7], target=9)
