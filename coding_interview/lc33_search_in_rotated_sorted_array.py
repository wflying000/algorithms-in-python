"""
https://leetcode.cn/problems/search-in-rotated-sorted-array
"""

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        
        return self.binary_search(nums, target)

    
    def binary_search(self, nums, target):
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[0]:
                if target >= nums[0] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target > nums[mid] and target <= nums[-1]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1



def main():
    sln = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 7
    res = sln.search(nums, target)
    print(res)


if __name__ == "__main__":
    main()