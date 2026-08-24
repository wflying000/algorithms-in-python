"""
https://leetcode.cn/problems/first-missing-positive
"""

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        原地置换：尽量把值 v 放到下标 v - 1 上。
        处理完后，第一个不满足 nums[i] == i + 1 的位置，
        就对应第一个缺失的正数 i + 1。
        """
        n = len(nums)

        for i in range(n):
            # nums[i] 必须能放进数组范围内的某个目标位置，
            # 并且目标位置上的值还没有放对，避免重复元素造成死循环。
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                target = nums[i] - 1
                nums[i], nums[target] = nums[target], nums[i]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1


def main():
    sln = Solution()
    nums = [3, 4, -1, 1]
    res = sln.firstMissingPositive(nums)
    print(res)


if __name__ == "__main__":
    main()