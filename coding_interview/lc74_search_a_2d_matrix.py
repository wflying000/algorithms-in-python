"""
https://leetcode.cn/problems/search-a-2d-matrix
"""

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        return self.binary_search(matrix, target)
    
    def binary_search(self, matrix, target):
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = (right - left) // 2 + left
            x = mid // n
            y = mid % n
            if matrix[x][y] < target:
                left = mid + 1
            elif matrix[x][y] > target:
                right = mid - 1
            else:
                return True
        
        return False


def main():
    sln = Solution()
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    res = sln.searchMatrix(matrix, target)
    print(res)


if __name__ == "__main__":
    main()