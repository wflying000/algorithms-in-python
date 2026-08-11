"""
https://leetcode.cn/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/description/?envType=study-plan-v2&envId=coding-interviews

https://leetcode.cn/problems/number-of-1-bits/
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n != 0:
            res += 1
            n = n & (n - 1)
        return res

def to_int32(x):
    x = x & 0xFFFFFFFF   # 先截断到32bit
    return x

def main():
    sln = Solution()
    num = to_int32(-1)
    print(num)
    res = sln.hammingWeight(num)
    print(res)


if __name__ == "__main__":
    main()