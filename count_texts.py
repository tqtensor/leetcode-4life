"""
Building our Intuition:
Let us imagine pressedKeys is "2222".

The only way to interpret "2" is:
["a"]

There are two ways we interpret "22":
["aa", "b"]

Four ways we interpret "222":
["aaa", "ba", "ab", "c"]

Seven ways we interpret "2222":
["aaaa", "baa", "aba", "ca", "aab", "bb", "ac"]

In each state we can see that to get the ways a digit is interpretting as ending with "a", 
we need to combine all digits that ended previously with "a", "b", & "c". Then to get the 
ways the str can be interpretted as ending with "b", it would be the number of strings 
that ended with "a" in our previous digit. Similarly for "c" we need to get the number of 
ways the previous str ended with "b".
"""


class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        if not pressedKeys:
            return 0

        MOD = 10**9 + 7
        chars_in_digit = {
            "2": 3,
            "3": 3,
            "4": 3,
            "5": 3,
            "6": 3,
            "7": 4,
            "8": 3,
            "9": 4,
        }

        prev_states = [1]
        prev_digit = None

        for digit in pressedKeys:
            total = sum(prev_states) % MOD

            if digit != prev_digit:
                prev_states = [total] + [0] * (chars_in_digit[digit] - 1)
            else:
                prev_states = [total] + prev_states[: chars_in_digit[digit] - 1]

            prev_digit = digit
        return sum(prev_states) % MOD


if __name__ == "__main__":
    print(Solution().countTexts(pressedKeys="2222"))
