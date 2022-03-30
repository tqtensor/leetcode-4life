from collections import defaultdict, deque
from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = defaultdict(int)
        for task in tasks:
            count[task] += 1

        pq, q = [-cnt for cnt in count.values()], deque()
        heapify(pq)

        time = 0
        while pq or q:
            if pq:
                cnt = heappop(pq) + 1  # the remaining number of tasks in this category
                if cnt < 0:
                    q.append(
                        (cnt, time + n)
                    )  # time + n is the time when this kind of task can be processed
            if q and q[0][1] == time:
                heappush(pq, q.popleft()[0])  # put back the kind of task
            time += 1

        return time


if __name__ == "__main__":
    Solution.leastInterval(object, tasks=["A", "A", "A", "B", "B", "C", "C"], n=2)
