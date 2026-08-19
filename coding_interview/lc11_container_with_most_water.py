"""
https://leetcode.cn/problems/container-with-most-water
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        i, j = 0, n - 1
        res = 0
        while i < j:
            if height[i] <= height[j]:
                area = height[i] * (j - i)
                i += 1
            else:
                area = height[j] * (j - i)
                j -= 1
            
            res = max(res, area)
        
        return res


def main():
    sln = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    res = sln.maxArea(height)
    print(res)


if __name__ == "__main__":
    main()