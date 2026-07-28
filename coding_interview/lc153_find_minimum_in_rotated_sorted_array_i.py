"""
https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/description/
"""

from typing import List

class Solution:
    def findMin1(self, nums: List[int]) -> int:
        n = len(nums)
        if nums[-1] > nums[0]:
            return nums[0]
        i, j = 0, n - 1
        res = nums[-1]
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] < nums[-1]:
                res = nums[mid]
                j = mid - 1
            else:
                i = mid + 1
        
        return res

    def findMin(self, nums):
        i, j = 0, len(nums) - 1
        while i < j:
            mid = (i + j) // 2
            if nums[mid] < nums[j]:
                j = mid
            else:
                i = mid + 1
        return nums[i]


def main():
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6, 7, 0, 1, 2]
    nums3 = [2, 3, 1]
    sln = Solution()
    print(sln.findMin(nums1))
    print(sln.findMin(nums2))
    print(sln.findMin(nums3))



if __name__ == "__main__":
    main()
