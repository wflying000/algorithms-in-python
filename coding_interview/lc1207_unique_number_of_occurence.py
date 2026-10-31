"""
https://leetcode.cn/problems/unique-number-of-occurrences
"""

from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        num2cnt = {}
        for x in arr:
            num2cnt[x] = num2cnt.get(x, 0) + 1
        return len(num2cnt) == len(set(num2cnt.values()))


def main():
    sln = Solution()
    arr = [1, 2, 2, 1, 1, 3]
    res = sln.uniqueOccurrences(arr)
    print(res)


if __name__ == "__main__":
    main()