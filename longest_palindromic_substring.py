class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        longest = ""

        for right in range(n):
            for left in range(right + 1):
                if s[right] == s[left] and (
                    (right + 1 - left) <= 3 or dp[right - 1][left + 1]
                ):
                    dp[right][left] = True
                    if right + 1 - left > len(longest):
                        longest = s[left : right + 1]
        return longest


if __name__ == "__main__":
    Solution.longestPalindrome(object, s="babad")
