"""
https://leetcode.cn/problems/sort-colors
"""

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low, mid, high = 0, 0, len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1


def main():
    sln = Solution()
    nums = [0, 1, 0, 2, 0, 1, 2]
    sln.sortColors(nums)
    print(nums)


if __name__ == "__main__":
    main()