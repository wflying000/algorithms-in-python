"""
https://leetcode.cn/problems/trapping-rain-water
"""

from typing import List


class Solution:

    def trap(self, height: List[int]) -> int:
        return self.trap3(height)

    def trap3(self, height):
        res = 0
        i, j = 0, len(height) - 1
        left_highest, right_highest = 0, 0
        while i < j:
            left_highest = max(left_highest, height[i])
            right_highest = max(right_highest, height[j])
            if height[i] < height[j]:
                res += left_highest - height[i]
                i += 1
            else:
                res += right_highest - height[j]
                j -= 1
        
        return res
    
    def trap2(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        highest = height[-1]
        right = [0] * n
        for i in range(n - 2, 0, -1):
            right[i] = highest
            highest = max(highest, height[i])

        left_highest = height[0]
        res = 0
        for i in range(1, n - 1):
            res += max(0, (min(left_highest, right[i]) - height[i]))
            left_highest = max(left_highest, height[i])

        return res

    def trap1(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        left = [0] * n
        right = [0] * n
        highest = height[0] 
        for i in range(1, n):
            left[i] = highest
            highest = max(highest, height[i])

        highest = height[-1]
        for i in range(n - 2, 0, -1):
            right[i] = highest
            highest = max(highest, height[i])

        res = 0
        for i in range(1, n - 1):
            res += max(0, (min(left[i], right[i]) - height[i]))

        return res


def main():
    sln = Solution()
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    res = sln.trap(height)
    print(res)


if __name__ == "__main__":
    main()