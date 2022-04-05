from functools import cache
from typing import List


class Solution:
    @cache
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(path, level):
            if level >= len(digits):
                ans.append(path)
                return
            letters = numpad[int(digits[level])]
            for i in range(len(letters)):
                path += letters[i]
                dfs(path, level + 1)
                path = path[:-1]  # similar with deque.pop()

        ans = []

        if len(digits) == 0:
            return ans

        path = ""
        level = 0
        numpad = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
        }
        dfs(path, level)
        return ans


if __name__ == "__main__":
    Solution.letterCombinations(object, digits="23")
