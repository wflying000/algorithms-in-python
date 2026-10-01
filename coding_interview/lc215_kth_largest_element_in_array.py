"""
https://leetcode.cn/problems/kth-largest-element-in-an-array
"""

from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        target = n - k
        return self.quick_select(nums, target, 0, n - 1)

    def quick_select(self, nums, k, left, right):
        if left == right:
            return nums[left]

        pivot = nums[(left + right) // 2]

        i, j = left - 1, right + 1

        while True:
            i += 1
            while nums[i] < pivot:
                i += 1

            j -= 1
            while nums[j] > pivot:
                j -= 1

            if i >= j:
                break

            nums[i], nums[j] = nums[j], nums[i]

        if k <= j:
            return self.quick_select(nums, k, left, j)
        else:
            return self.quick_select(nums, k, j + 1, right)


def main():
    sln = Solution()
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    res = sln.findKthLargest(nums, k)
    print(res)


if __name__ == "__main__":
    main()