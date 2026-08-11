"""
https://leetcode.cn/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/?envType=study-plan-v2&envId=coding-interviews
"""

class Solution:
    def encryptionCalculate(self, dataA: int, dataB: int) -> int:
        x = 0xffffffff
        a, b = dataA & x, dataB & x
        while b != 0:
            c = ((a & b) << 1) & x
            a = a ^ b 
            b = c 
        
        # 如果a是正数，则直接返回 
        if a <= 0x7fffffff: 
            return a 
        else:
            # a为负数，需要将a转为负数表示
            return ~(a ^ x)


def main():
    sln = Solution()
    a = 10
    b = -2
    res = sln.encryptionCalculate(a, b)
    assert res == a + b


if __name__ == "__main__":
    main()