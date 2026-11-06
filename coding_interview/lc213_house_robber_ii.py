"""
https://leetcode.cn/problems/house-robber-ii
"""

class Solution:
    def rob(self, nums: list[int]) -> int:
        
        def rob_range(start, end):
            a, b = 0, nums[start]
            for i in range(start + 1, end + 1):
                ta = max(a, b)
                tb = a + nums[i]
                a, b = ta, tb
            return max(a, b)
        
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])
            
        return max(rob_range(0, n - 2), rob_range(1, n - 1))


def main():
    sln = Solution()
    nums = [1, 2, 3, 1]
    res = sln.rob(nums)
    print(res)


if __name__ == "__main__":
    main()