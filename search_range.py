from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]

        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                ans[0] = mid
                high = mid - 1
            if nums[mid] > target:
                high = mid - 1
            if nums[mid] < target:
                low = mid + 1

        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                ans[1] = mid
                low = mid + 1
            if nums[mid] > target:
                high = mid - 1
            if nums[mid] < target:
                low = mid + 1

        return ans


if __name__ == "__main__":
    Solution.searchRange(object, nums=[5, 7, 7, 8, 8, 10], target=8)
