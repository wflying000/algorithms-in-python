"""
https://leetcode.cn/problems/maximum-average-subarray-i
"""

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        s = 0
        for i in range(k):
            s += nums[i]
        res = s / k
        for i in range(k, len(nums)):
            s = s - nums[i - k] + nums[i]
            res = max(res, s / k)
        return res

def main():
    sln = Solution()
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    res = sln.findMaxAverage(nums, k)
    print(res)


if __name__ == "__main__":
    main()