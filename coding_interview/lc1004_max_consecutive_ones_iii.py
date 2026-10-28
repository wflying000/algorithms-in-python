"""
https://leetcode.cn/problems/max-consecutive-ones-iii
"""


class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        i, res, cnt = 0, 0, 0
        for j, num in enumerate(nums):
            cnt += 1 - num 
            while cnt > k:
                cnt -= 1 - nums[i]
                i += 1
            res = max(res, j - i + 1)
        return res


def main():
    sln = Solution()
    nums = [1,1,1,0,0,0,1,1,1,1,0]
    k = 2
    res = sln.longestOnes(nums, k)
    print(res)


if __name__ == "__main__":
    main()