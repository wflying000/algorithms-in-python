"""
https://leetcode.cn/problems/kids-with-the-greatest-number-of-candies
"""

from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_num = max(candies)
        res = []
        for i, num in enumerate(candies):
            if num + extraCandies >= max_num:
                res.append(True)
            else:
                res.append(False)
        return res


def main():
    sln = Solution()
    candies = [2, 3, 5, 1, 3]
    extraCandies = 3
    res = sln.kidsWithCandies(candies, extraCandies)
    print(res)


if __name__ == "__main__":
    main()