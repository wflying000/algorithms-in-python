"""
https://leetcode.cn/problems/jump-game
"""

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n = len(nums)
        max_dist = 0
        for i in range(n):
            if i <= max_dist:
                max_dist = max(max_dist, i + nums[i])
            else:
                break
        return max_dist >= n - 1


def main():
    sln = Solution()
    nums = [2, 3, 1, 1, 4]
    res = sln.canJump(nums)
    print(res)


if __name__ == "__main__":
    main()