"""
https://leetcode.cn/problems/set-matrix-zeroes/
"""

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        set_row_0, set_col_0 = False, False 
        for i in range(n):
            if matrix[0][i] == 0:
                set_row_0 = True
                break
        for i in range(m):
            if matrix[i][0] == 0:
                set_col_0 = True

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if set_row_0:
            for i in range(n):
                matrix[0][i] = 0
        
        if set_col_0:
            for i in range(m):
                matrix[i][0] = 0


def main():
    sln = Solution()
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    sln.setZeroes(matrix)
    print(matrix)

if __name__ == "__main__":
    main()