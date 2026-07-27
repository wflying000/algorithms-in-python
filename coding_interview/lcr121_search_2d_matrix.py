"""
https://leetcode.cn/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/description/?envType=study-plan-v2&envId=coding-interviews

https://leetcode.cn/problems/search-a-2d-matrix-ii/
"""

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1
        while i < m and j >= 0:
            if matrix[i][j] < target:
                i += 1
            elif matrix[i][j] > target:
                j -= 1
            else:
                return True
        
        return False

def main():
    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    target = 5
    sln = Solution()
    res = sln.searchMatrix(matrix, target)
    print(res)


if __name__ == "__main__":
    main()