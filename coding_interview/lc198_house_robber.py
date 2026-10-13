"""
https://leetcode.cn/problems/house-robber
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        a, b = 0, nums[0]
        n = len(nums)
        for i in range(1, n):
            ta = max(a, b)
            tb = a + nums[i]
            a, b = ta, tb
        
        return max(a, b)


def main():
    sln = Solution()
    nums = [2, 7, 9, 3, 1]
    res = sln.rob(nums)
    print(res)


if __name__ == "__main__":
    main()