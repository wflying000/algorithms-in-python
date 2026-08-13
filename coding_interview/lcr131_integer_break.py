"""
https://leetcode.cn/problems/jian-sheng-zi-lcof/description/?envType=study-plan-v2&envId=coding-interviews

https://leetcode.cn/problems/integer-break/
"""

class Solution:
    def cuttingBamboo(self, bamboo_len: int) -> int:
        n = bamboo_len
        if n == 2:
            return 1
        if n == 3:
            return 2
        r = n % 3
        q = n // 3
        if r == 0:
            return 3 ** q
        elif r == 1:
            return (3 ** (q - 1)) * 4
        else:
            # r == 2:
            return (3 ** q) * 2

def main():
    sln = Solution()
    nums = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    labels = [1, 2, 4, 6, 9, 12, 18, 27, 36]

    for num, label in zip(nums, labels):
        res = sln.cuttingBamboo(num)
        assert res == label


if __name__ == "__main__":
    main()