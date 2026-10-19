"""
https://leetcode.cn/problems/greatest-common-divisor-of-strings
"""

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcd_len = self.gcd(len(str1), len(str2))
        gcd_str = str1[:gcd_len]
        if str1 + str2 == str2 + str1:
            return gcd_str
        return ""

    
    def gcd(self, m, n):
        r = m % n
        while r != 0:
            m = n
            n = r 
            r = m % n
        return n


def main():
    sln = Solution()
    str1 = "ABABAB"
    str2 = "ABAB"
    res = sln.gcdOfStrings(str1, str2)
    print(res)


if __name__ == "__main__":
    main()