"""
https://leetcode.cn/problems/equal-row-and-column-pairs/
"""

from typing import List
from collections import Counter


class Solution:

    def equalPairs(self, grid):
        res, n = 0, len(grid)
        counts = Counter(tuple(row) for row in grid)
        res = 0
        for j in range(n):
            col = tuple([grid[i][j] for i in range(n)])
            res += counts[col]
        return res

    def equalPairs_1(self, grid: List[List[int]]) -> int:
        n = len(grid)
        res = 0
        for row in range(n):
            for col in range(n):
                if self.equal(grid, row, col):
                    res += 1
        return res

    
    def equal(self, grid, row, col):
        n = len(grid)
        for i in range(n):
            if grid[row][i] != grid[i][col]:
                return False

        return True


def main():
    sln = Solution()
    grid = [[3,2,1],[1,7,6],[2,7,7]]
    res = sln.equalPairs(grid)
    print(res)


if __name__ == "__main__":
    main()