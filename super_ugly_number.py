from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        nums = primes.copy()  # do a deep copy
        heapify(nums)  # create a heap
        p = 1
        for _ in range(n - 1):
            p = heappop(nums)  # take the smallest element
            for prime in primes:
                heappush(
                    nums, p * prime
                )  # add all those multiples with the smallest number
                if p % prime == 0:
                    break

        return p


if __name__ == "__main__":
    Solution.nthSuperUglyNumber(
        object,
        n=1000000,
        primes=[
            2,
            3,
            5,
            7,
            11,
            13,
            17,
            19,
            23,
            29,
            31,
            37,
            41,
            43,
            47,
            53,
            59,
            61,
            67,
            71,
            73,
            79,
            83,
            89,
            97,
            101,
            103,
            107,
            109,
            113,
            127,
            131,
            137,
            139,
            149,
            151,
            157,
            163,
            167,
            173,
            179,
            181,
            191,
            193,
            197,
            199,
            211,
            223,
            227,
            229,
            233,
            239,
            241,
            251,
            257,
            263,
            269,
            271,
            277,
            281,
            283,
            293,
            307,
            311,
            313,
            317,
            331,
            337,
            347,
            349,
            353,
            359,
            367,
            373,
            379,
            383,
            389,
            397,
            401,
            409,
            419,
            421,
            431,
            433,
            439,
            443,
            449,
            457,
            461,
            463,
            467,
            479,
            487,
            491,
            499,
            503,
            509,
            521,
            523,
            541,
        ],
    )
