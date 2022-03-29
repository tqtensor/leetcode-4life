from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        print(nums.__add__)
        for pivot in range(len(nums))[::-1]:
            if nums[pivot - 1] < nums[pivot]:
                pivot -= 1
                break

        if pivot == -1:
            nums[:] = nums[::-1]
        else:
            for j in range(len(nums))[::-1]:
                if nums[j] > nums[pivot]:
                    nums[pivot], nums[j] = nums[j], nums[pivot]
                    break
            nums[pivot + 1 :] = nums[pivot + 1 :][::-1]

        print(nums.__add__)
        print(nums)


if __name__ == "__main__":
    Solution.nextPermutation(object, nums=[3, 2, 1])
