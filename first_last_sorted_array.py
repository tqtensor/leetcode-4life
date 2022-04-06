from typing import List
from bisect import bisect_left, bisect_right


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]

        left, right = 0, len(nums) - 1
        mid = (left + right) // 2
        nums.append(float("inf"))

        while (nums[left] != target) | (nums[right] != target):
            if right - left == 1:
                if target == nums[left]:
                    return [left, left]
                elif target == nums[right]:
                    return [right, right]
                else:
                    return [-1, -1]

            if nums[mid] < target:
                left = mid
                mid = (left + right) // 2
            elif nums[mid] > target:
                right = mid
                mid = (left + right) // 2
            else:
                return [
                    bisect_left(nums, target, lo=left, hi=right),
                    bisect_right(nums, target, lo=left, hi=right + 1) - 1,
                ]
        return [left, right]


if __name__ == "__main__":
    print(Solution.searchRange(object, nums=[1, 2, 2], target=2))
