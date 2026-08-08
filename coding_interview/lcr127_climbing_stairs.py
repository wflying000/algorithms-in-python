"""
https://leetcode.cn/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/description/?envType=study-plan-v2&envId=coding-interviews

https://leetcode.cn/problems/climbing-stairs/
"""

class Solution:
    def trainWays(self, num: int) -> int:
        a, b, s = 1, 0, 1
        MOD = int(1e9 + 7)
        for i in range(num):
            a = b
            b = s
            s = (a + b) % MOD
        
        return s


def main():
    nums = [1, 1, 2, 3, 5, 8, 13]
    sln = Solution()
    for idx, num in enumerate(nums):
        res = sln.trainWays(idx)
        assert res == num


if __name__ == "__main__":
    main()