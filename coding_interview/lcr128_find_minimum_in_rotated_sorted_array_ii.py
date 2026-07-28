"""
https://leetcode.cn/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/description/?envType=study-plan-v2&envId=coding-interviews

https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array-ii/description/


已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。例如，原数组 nums = [0,1,4,4,5,6,7] 在变化后可能得到：
若旋转 4 次，则可以得到 [4,5,6,7,0,1,4]
若旋转 7 次，则可以得到 [0,1,4,4,5,6,7]
注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], ..., a[n-2]] 。

给你一个可能存在 重复 元素值的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。

你必须尽可能减少整个过程的操作步骤。

"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        i, j = 0, n - 1
        while i < j:
            mid = i + (j - i) // 2
            if nums[mid] < nums[j]:
                j = mid
            elif nums[mid] > nums[j]:
                i = mid + 1
            else:
                j -= 1
        return nums[i]


def main():
    nums1 = [1, 3, 5]
    nums2 = [2, 2, 2, 0, 1]
    nums3 = [3, 1, 3]
    sln = Solution()
    print(sln.findMin(nums1))
    print(sln.findMin(nums2))
    print(sln.findMin(nums3))


if __name__ == "__main__":
    main()