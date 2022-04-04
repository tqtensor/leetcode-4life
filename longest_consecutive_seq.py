from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums = set(nums)
        sequences = []

        for num in nums:
            if num - 1 not in nums:
                for i in range(1, len(nums) + 1):
                    if num + i not in nums:
                        sequences.append(i)
                        break
        return max(sequences)


if __name__ == "__main__":
    Solution.longestConsecutive(object, nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
