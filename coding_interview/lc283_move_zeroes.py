"""
https://leetcode.cn/problems/move-zeroes
"""

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # idx = 0
        # for num in nums:
        #     if num != 0:
        #         nums[idx] = num 
        #         idx += 1
        # nums[idx : len(nums)] = [0] * (len(nums) - idx)

        k = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[k] = nums[k], nums[i]
                k += 1
                


def main():
    sln = Solution()
    nums = [0, 1, 0, 3, 2]
    sln.moveZeroes(nums)
    print(nums)


if __name__ == "__main__":
    main()