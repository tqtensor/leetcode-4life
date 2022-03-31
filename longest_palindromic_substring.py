class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        longest = ""

        for right in range(n - 1, -1, -1):
            for left in range(right):
                if right == left:  # base case 1
                    dp[right][left] = True

                if s[right] == s[left]:
                    if right - left == 1:
                        dp[right][left] = True  # base case 2
                    else:
                        dp[right][left] = dp[right - 1][left + 1]

                if dp[right][left]:
                    if right + 1 - left > len(longest):
                        longest = s[left : right + 1]
        return longest


if __name__ == "__main__":
    Solution.longestPalindrome(object, s="babad")
