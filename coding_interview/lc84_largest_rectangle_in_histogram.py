"""
https://leetcode.cn/problems/largest-rectangle-in-histogram
"""

from collections import deque


class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        n = len(heights)
        stack = deque()
        left, right = [0] * n, [0] * n

        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)
        stack = deque()
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)
        
        res = max((right[i] - left[i] - 1) * heights[i] for i in range(n))
        return res



def main():
    sln = Solution()
    heights = [2, 1, 5, 6, 2, 3]
    res = sln.largestRectangleArea(heights)
    print(res)


if __name__ == "__main__":
    main()