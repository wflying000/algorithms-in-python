"""
https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array
"""

from typing import List


class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        # return self.search_range_1(nums, target)

        return self.search_range_2(nums, target)
    
    def search_range_2(self, nums, target):
        first = self.binary_search(nums, target, True)
        last = self.binary_search(nums, target, False) - 1
        if first <= last and last < len(nums) and nums[first] == target and nums[last] == target:
            return [first, last]

        return [-1, -1]

    def binary_search(self, nums, target, equal):
        res = len(nums)
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if (nums[mid] > target) or (equal and nums[mid] >= target):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res



    def search_range_1(self, nums, target):
        first = self.search_first(nums, target)
        if first == -1:
            return [-1, -1]
        last = self.search_last(nums, target)
        return [first, last]

    def search_first(self, nums, target):
        res = -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                res = mid
                right = mid - 1
        return res

    def search_last(self, nums, target):
        res = -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                res = mid
                left = mid + 1
        return res    


def main():
    sln = Solution()
    nums = [5, 7, 7, 8, 8, 10] 
    target = 8
    res = sln.searchRange(nums, target)
    print(res)


if __name__ == "__main__":
    main()