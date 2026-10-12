"""
https://leetcode.cn/problems/climbing-stairs
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        a, b, s = 0, 0, 1
        for _ in range(n):
            a = b
            b = s
            s = a + b
        
        return s


def main():
    sln = Solution()
    n = 10
    res = sln.climbStairs(n)
    print(res)


if __name__ == "__main__":
    main()