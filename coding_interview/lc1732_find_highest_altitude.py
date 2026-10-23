"""
https://leetcode.cn/problems/find-the-highest-altitude
"""

from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res, h = 0, 0
        for i in range(len(gain)):
            h += gain[i]
            res = max(res, h)
        return res


def main():
    sln = Solution()
    gain = [-5, 1, 5, 0, -7]
    res = sln.largestAltitude(gain)
    print(res)


if __name__ == "__main__":
    main()