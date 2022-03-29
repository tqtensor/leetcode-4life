from typing import List


class Solution:
    def sort_dict(self, d: dict) -> dict:
        return {
            k: v for k, v in sorted(d.items(), reverse=True, key=lambda item: item[1])
        }

    def leastInterval(self, tasks: List[str], n: int) -> int:
        dictMap = {}
        for task in tasks:
            if dictMap.get(task) is None:
                dictMap[task] = 1
            else:
                dictMap[task] += 1
        dictMap = self.sort_dict(dictMap)

        k = n + 1
        count = 0

        while dictMap:
            taskComp = 0
            removeTask = []
            for task in dictMap:
                if taskComp == k:
                    break
                if dictMap[task] > 0:
                    dictMap[task] -= 1
                    if dictMap[task] == 0:
                        removeTask.append(task)
                taskComp += 1
            for task in removeTask:
                dictMap.pop(task)
            dictMap = self.sort_dict(dictMap)
            if dictMap:
                count += k
            else:
                count += taskComp

        return count


if __name__ == "__main__":
    s = Solution()
    s.leastInterval(tasks=["A", "A", "A", "B", "B", "C", "C"], n=2)
