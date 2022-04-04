from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            supplements = set()
            results = []
            for num in nums:
                if target - num not in supplements:
                    supplements.add(num)
                else:
                    results.append([num, target - num])
            return results

        nums = sorted(nums)
        n = len(nums)
        results = set()

        for i in range(n):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:  # already scanned through
                continue

            if (
                nums[n - 1] + nums[n - 2] >= -nums[i]
            ):  # nums[n-1] + nums[n-2] is the largest 2sum we can get
                supplements = nums[i + 1 : n]
            else:
                supplements = None

            if supplements:
                pairs = twoSum(nums=supplements, target=-nums[i])
                if len(pairs) > 0:
                    for pair in pairs:
                        if (nums[i], pair[0], pair[1]) not in results:
                            results.add((nums[i], pair[0], pair[1]))
        return [list(r) for r in list(results)]


if __name__ == "__main__":
    Solution.threeSum(object, nums=[-1, 0, 1, 2, -1, -4])
