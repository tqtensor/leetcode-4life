import math
from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x: int, y: int) -> float:
            return math.sqrt(x**2 + y**2)

        dists = []
        heapify(dists)
        for _ in range(k):
            x, y = points.pop()
            heappush(dists, (-distance(x, y), [x, y]))

        while points:
            x, y = points.pop()
            if distance(x, y) < -dists[0][0]:
                heappop(dists)
                heappush(dists, (-distance(x, y), [x, y]))

        return [dist[1] for dist in dists]


if __name__ == "__main__":
    Solution.kClosest(object, points=[[3, 3], [5, -1], [-2, 4]], k=2)
