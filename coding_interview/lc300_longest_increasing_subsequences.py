"""
https://leetcode.cn/problems/longest-increasing-subsequence
"""

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [1] * n
        res = 1
        for i in range(1, n):
            max_len = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    max_len = max(max_len, dp[j])
            dp[i] = max_len + 1
            res = max(res, dp[i])
        return res


def main():
    sln = Solution()
    nums = [0, 1, 0, 3, 2, 3]
    res = sln.lengthOfLIS(nums)
    print(res)


if __name__ == "__main__":
    main()