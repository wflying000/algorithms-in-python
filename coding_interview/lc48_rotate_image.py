"""
https://leetcode.cn/problems/rotate-image
"""

from typing import List


class Solution:

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        n = len(matrix)
        lx, ly, rx, ry = 0, 0, n - 1, n - 1
        # 从外层到内层逐层旋转
        while lx < rx:
            dy = ry - ly
            for j in range(dy):
                tmp = matrix[lx][ly + j]
                matrix[lx][ly + j] = matrix[rx - j][ly] # 上面一行从左到右 由 左边一列从下到上填充
                matrix[rx - j][ly] = matrix[rx][ry - j] # 左边一列从下到上 由 下面一行从右到左填充
                matrix[rx][ry - j] = matrix[lx + j][ry] # 下面一行从右到左 由 右边一列从上到下填充
                matrix[lx + j][ry] = tmp                # 右边一列从上到下 由 上面一行从左到右填充
            lx += 1
            ly += 1
            rx -= 1
            ry -= 1
        

def main():
    sln = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    sln.rotate(matrix)
    print(matrix)


if __name__ == "__main__":
    main()