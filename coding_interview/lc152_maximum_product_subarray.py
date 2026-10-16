"""
https://leetcode.cn/problems/maximum-product-subarray
"""

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        minimum, maximum = nums[0], nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            t1 = minimum * nums[i]
            t2 = maximum * nums[i]
            minimum = min(t1, t2, nums[i])
            maximum = max(t1, t2, nums[i])
            res = max(res, maximum)
        
        return res


def main():
    sln = Solution()
    nums = [2, 3, -2, 4]
    res = sln.maxProduct(nums)
    print(res)


if __name__ == "__main__":
    main()