class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        res = ""

        def spread(i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i + 1 : j]

        for i in range(n):
            res = max(spread(i, i), spread(i, i + 1), res, key=len)
        return res


if __name__ == "__main__":
    Solution.longestPalindrome(object, s="babad")
