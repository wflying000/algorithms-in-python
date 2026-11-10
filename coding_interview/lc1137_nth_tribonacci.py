"""
https://leetcode.cn/problems/n-th-tribonacci-number
"""

class Solution:
    def tribonacci(self, n: int) -> int:
        a, b, c = 0, 1, 1
        if n == 0:
            return 0
        elif n <= 2:
            return 1
        for _ in range(n - 2):
            a, b, c = b, c, a + b + c
        return c


def main():
    sln = Solution()
    n = 5
    res = sln.tribonacci(n)
    print(res)


if __name__ == "__main__":
    main()
