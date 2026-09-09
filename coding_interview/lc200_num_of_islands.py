"""
https://leetcode.cn/problems/number-of-islands
"""

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        res = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "1":
                    res += 1
                    self.dfs(grid, x, y)
        return res

    def dfs(self, grid, x, y):
        dxs = [-1, 1, 0, 0]
        dys = [0, 0, -1, 1]
        m, n = len(grid), len(grid[0])

        grid[x][y] = "0"
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if nx >= 0 and nx < m and ny >= 0 and ny < n and grid[nx][ny] == "1":
                self.dfs(grid, nx, ny)


def main():
    sln = Solution()
    grid = [
        ['1','1','0','0','0'],
        ['1','1','0','0','0'],
        ['0','0','1','0','0'],
        ['0','0','0','1','1']
    ]
    res = sln.numIslands(grid)
    print(res)



if __name__ == "__main__":
    main()