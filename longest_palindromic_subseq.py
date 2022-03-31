from functools import cache


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @cache
        def find_palindrome(left, right):
            if right - left <= 0:
                return right - left + 1
            if s[left] == s[right]:
                return 2 + find_palindrome(left + 1, right - 1)
            return max(
                find_palindrome(left + 1, right), find_palindrome(left, right - 1)
            )

        return find_palindrome(0, len(s) - 1)


if __name__ == "__main__":
    Solution.longestPalindromeSubseq(object, s="bbbab")
