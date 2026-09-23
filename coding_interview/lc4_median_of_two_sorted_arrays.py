"""
https://leetcode.cn/problems/median-of-two-sorted-arrays/
"""

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # 在较短的数组上二分，保证 j 不会越界
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left_count = (m + n + 1) // 2
        left, right = 0, m
        neg_inf, pos_inf = float("-inf"), float("inf")

        while left <= right:
            # nums1 左半段取 i 个，nums2 左半段取 left_count - i 个
            i = left + (right - left) // 2
            j = left_count - i

            nums1_left = neg_inf if i == 0 else nums1[i - 1]
            nums1_right = pos_inf if i == m else nums1[i]
            nums2_left = neg_inf if j == 0 else nums2[j - 1]
            nums2_right = pos_inf if j == n else nums2[j]

            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                # 找到了正确的分割线
                if (m + n) % 2 == 1:
                    return float(max(nums1_left, nums2_left))

                return (
                    max(nums1_left, nums2_left)
                    + min(nums1_right, nums2_right)
                ) / 2

            if nums1_left > nums2_right:
                # nums1 左半段太大，分割线左移
                right = i - 1
            else:
                # nums1 左半段太小，分割线右移
                left = i + 1

        raise ValueError("input arrays must be sorted")


def main():
    sln = Solution()
    print(sln.findMedianSortedArrays([1, 3], [2]))       # 2.0
    print(sln.findMedianSortedArrays([1, 2], [3, 4]))    # 2.5


if __name__ == "__main__":
    main()
