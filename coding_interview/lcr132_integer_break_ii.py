"""
https://leetcode.cn/problems/jian-sheng-zi-ii-lcof/description/?envType=study-plan-v2&envId=coding-interviews
"""

class Solution:
    def cuttingBamboo(self, bamboo_len: int) -> int:

        if bamboo_len < 4:
            return bamboo_len - 1
        n = bamboo_len
        MOD = int(1e9 + 7)
        q = n // 3
        r = n % 3

        if r == 1:
            res = 4
            for i in range(q - 1):
                res = (res * 3) % MOD 
        elif r == 2:
            res = 2
            for i in range(q):
                res = (res * 3) % MOD
        else:
            res = 1
            for i in range(q):
                res = (res * 3) % MOD

        return res
    
def main():
    sln = Solution()
    nums = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    labels = [1, 2, 4, 6, 9, 12, 18, 27, 36]

    for num, label in zip(nums, labels):
        res = sln.cuttingBamboo(num)
        assert res == label


if __name__ == "__main__":
    main()
