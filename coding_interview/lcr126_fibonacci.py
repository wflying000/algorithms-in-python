"""
https://leetcode.cn/problems/fei-bo-na-qi-shu-lie-lcof/description/?envType=study-plan-v2&envId=coding-interviews
"""


class Solution:
    def fib(self, n: int) -> int:
        a, b, s = 0, 1, 0
        MOD = int(1e9 + 7)
        for i in range(n):
            a = b
            b = s 
            s = (a + b) % MOD
        
        return s


def main():
    fibonacci_nums = [0, 1, 1, 2, 3, 5, 8, 13]
    sln = Solution()
    for idx, num in enumerate(fibonacci_nums):
        res = sln.fib(idx)
        assert res == num


if __name__ == "__main__":
    main()