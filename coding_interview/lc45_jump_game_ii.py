"""
https://leetcode.cn/problems/jump-game-ii
"""

class Solution:

    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        max_pos, end, step = 0, 0, 0
        for i in range(n - 1):
            max_pos = max(max_pos, i + nums[i])
            if i == end:
                end = max_pos
                step += 1
        return step


def main():
    sln = Solution()
    nums = [2, 3, 1, 1, 4]
    res = sln.jump(nums)
    print(res)


if __name__ == "__main__":
    main()