from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int):
        rows, cols = len(matrix), len(matrix[0])
        heap = []
        heapify(heap)
        for i in range(min(cols, k)):
            heappush(heap, (matrix[0][i], 0, i))

        for i in range(k - 1):
            _, r, c = heappop(heap)
            if r + 1 < rows:
                heappush(heap, (matrix[r + 1][c], r + 1, c))

        return heappop(heap)[0]


if __name__ == "__main__":
    Solution.kthSmallest(object, matrix=[[1, 5, 9], [10, 11, 13], [12, 13, 15]], k=8)
