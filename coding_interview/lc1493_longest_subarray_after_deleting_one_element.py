"""
https://leetcode.cn/problems/longest-subarray-of-1s-after-deleting-one-element
"""

class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        res, i, cnt = 0, 0, 0
        for j, num in enumerate(nums):
            cnt += 1 - num 
            while cnt > 1:
                cnt -= 1 - nums[i]
                i += 1
            res = max(res, j - i)
        return res


def main():
    sln = Solution()
    nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]
    res = sln.longestSubarray(nums)
    print(res)


if __name__ == "__main__":
    main()