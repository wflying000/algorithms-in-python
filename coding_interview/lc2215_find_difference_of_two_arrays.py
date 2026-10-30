"""
https://leetcode.cn/problems/find-the-difference-of-two-arrays/
"""

class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        diff1 = set(nums1).difference(nums2)
        diff2 = set(nums2).difference(nums1)
        return [list(diff1), list(diff2)]



def main():
    sln = Solution()
    nums1 = [1, 2, 3]
    nums2 = [2, 4, 6]
    res = sln.findDifference(nums1, nums2)
    print(res)


if __name__ == "__main__":
    main()