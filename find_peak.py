from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2

        while left != right:
            if nums[mid] > nums[mid + 1]:  # Decreasing part
                right = mid
            else:  # Increasing part
                left = mid + 1
            mid = (left + right) // 2
        return left


if __name__ == "__main__":
    Solution.findPeakElement(object, nums=[1, 2, 1, 3, 5, 6, 4])
