"""
https://leetcode.cn/problems/subarray-sum-equals-k
"""

from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        res = 0
        presum = 0
        sum2count = {0: 1}
        for i in range(len(nums)):
            presum = presum + nums[i]
            res += sum2count.get(presum - k, 0)
            sum2count[presum] = sum2count.get(presum, 0) + 1
        
        return res


def main():
    sln = Solution()
    nums = [-1, 0, 1, 1, 2]
    k = 2
    res = sln.subarraySum(nums, k)
    print(res)


if __name__ == "__main__":
    main()