"""
https://leetcode.cn/problems/increasing-triplet-subsequence
"""

class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        small, mid = float('inf'), float('inf')
        for num in nums:
            if num <= small:
                small = num
            elif num <= mid:
                mid = num
            elif num > mid:
                return True
        return False


def main():
    sln = Solution()
    nums = [1, 1, -2, 6]
    res = sln.increasingTriplet(nums)
    print(res)


if __name__ == "__main__":
    main()