"""
https://leetcode.cn/problems/max-number-of-k-sum-pairs/
"""

from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        res = 0
        num2cnt = {}
        for num in nums:
            diff = k - num
            if num2cnt.get(diff, 0) > 0:
                num2cnt[diff] -= 1
                res += 1
            else:
                num2cnt[num] = num2cnt.get(num, 0) + 1
        return res


def main():
    sln = Solution()
    nums = [1, 2, 3, 4]
    k = 5
    res = sln.maxOperations(nums, k)
    print(res)


if __name__ == "__main__":
    main()