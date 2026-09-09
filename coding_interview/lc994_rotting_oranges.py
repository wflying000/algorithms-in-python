"""
https://leetcode.cn/problems/rotting-oranges
"""
from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        queue = deque()
        num_good = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    num_good += 1
                elif grid[i][j] == 2:
                    queue.append([i, j])
        res = 0
        dxs = [-1, 1, 0, 0]
        dys = [0, 0, -1, 1]
        while queue:
            if num_good <= 0:
                break
            size = len(queue)
            for i in range(size):
                x, y = queue.popleft()
                for dx, dy in zip(dxs, dys):
                    nx, ny = x + dx, y + dy 
                    if nx >=0 and nx < m and ny >= 0 and ny < n and grid[nx][ny] == 1:
                        num_good -= 1
                        grid[nx][ny] = 2
                        queue.append([nx, ny])
            res += 1
        
        return res if num_good <= 0 else -1


def main():
    sln = Solution()
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    res = sln.orangesRotting(grid)
    print(res)


if __name__ == "__main__":
    main()