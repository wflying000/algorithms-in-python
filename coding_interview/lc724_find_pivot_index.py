"""
https://leetcode.cn/problems/find-pivot-index
"""

class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total = sum(nums)
        s = 0
        for i in range(len(nums)):
            if 2 * s + nums[i] == total:
                return i 
            s += nums[i]
        return -1


def main():
    sln = Solution()
    nums = [1, 7, 3, 6, 5, 6]
    res = sln.pivotIndex(nums)
    print(res)


if __name__ == "__main__":
    main()