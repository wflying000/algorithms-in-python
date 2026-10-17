"""
https://leetcode.cn/problems/partition-equal-subset-sum
"""

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False
        target = sum(nums)
        if target % 2 != 0:
            return False
        target = target // 2
        if target < max(nums):
            return False
        
        dp = [False] * (target + 1)
        dp[0], dp[nums[0]] = True, True
        for i in range(1, n):
            for j in range(target, 0, -1):
                if j >= nums[i]:
                    dp[j] = dp[j] or dp[j - nums[i]]
        
        return dp[target]




    def canPartition_2d(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False
        target = sum(nums)
        if target % 2 != 0:
            return False
        target = target // 2
        if target < max(nums):
            return False
        
        dp = [[False] * (target + 1) for _ in range(n)]
        dp[0][nums[0]] = True
        for i in range(n):
            dp[i][0] = True
        
        for i in range(1, n):
            for j in range(1, target + 1):
                if j >= nums[i]:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return dp[n - 1][target]



def main():
    sln = Solution()
    nums = [1, 5, 11, 5]
    res = sln.canPartition(nums)
    print(res)


if __name__ == "__main__":
    main()