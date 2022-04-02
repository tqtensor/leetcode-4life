from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        i, j = 0, 0
        output = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                output.append(nums1[i])
                i += 1
            else:
                output.append(nums2[j])
                j += 1

        if i < len(nums1):
            output.extend(nums1[i:])
        if j < len(nums2):
            output.extend(nums2[j:])

        if len(output) % 2 != 0:
            return output[len(output) // 2]
        else:
            mid = len(output) // 2
            return float(output[mid - 1] + output[mid]) / 2
