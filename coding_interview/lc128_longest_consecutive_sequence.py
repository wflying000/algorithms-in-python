"""
https://leetcode.cn/problems/longest-consecutive-sequence/
"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num_set = set(nums)
        res = 0
        for num in num_set:
            if num - 1 in num_set:
                continue
            cur = 1
            while num + 1 in num_set:
                cur += 1
                num += 1
            res = max(res, cur)
            
        return res

def main():
    sln = Solution()
    nums = [100, 4, 200, 1, 3, 2]
    res = sln.longestConsecutive(nums)
    print(res)


if __name__ == "__main__":
    main()