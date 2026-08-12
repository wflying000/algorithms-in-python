"""
https://leetcode.cn/problems/single-number-ii/description/
"""

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(32):
            num = 0
            for x in nums:
                num += (x >> i) & 1
            num = num % 3
            num = num << i 
            res = res | num
        
        # 需要考虑负数
        return res if res <= 0x7fffffff else ~(res ^ 0xffffffff)


def main():
    sln = Solution()
    nums1 = [2, 2, 3, 2]
    res1 = sln.singleNumber(nums1)
    print(res1)

    nums2 = [-1, -1, -1, -5]
    res2 = sln.singleNumber(nums2)
    print(res2)

    nums3 = [-1, -1, -1, 10]
    res3 = sln.singleNumber(nums3)
    print(res3)

    nums4 = [1, 1, 1, -100]
    res4 = sln.singleNumber(nums4)
    print(res4)


if __name__ == "__main__":
    main()