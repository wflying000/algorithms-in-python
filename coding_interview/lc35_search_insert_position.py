"""
https://leetcode.cn/problems/search-insert-position
"""

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        
        return self.binary_search(nums, target)

    def binary_search(self, nums, target):
        n = len(nums)
        res = n
        left, right = 0, n - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if nums[mid] < target:
                left = mid + 1
            else:
                res = mid
                right = mid - 1
        return res



def main():
    sln = Solution()
    nums = [1, 2, 4, 5]
    target = 3
    res = sln.searchInsert(nums, target)
    print(res)


if __name__ == "__main__":
    main()