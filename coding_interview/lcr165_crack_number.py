"""
https://leetcode.cn/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/description/?envType=study-plan-v2&envId=coding-interviews

https://leetcode.cn/problems/decode-ways/description/
"""


class Solution:

    def crackNumber(self, ciphertext: int) -> int:

        return self.crack_number_1(ciphertext)

    def crack_number_1(self, ciphertext: int) -> int:
        chs = str(ciphertext)
        n = len(chs)
        dp = [0 for _ in range(n + 1)]
        dp[0], dp[1] = 1, 1
        for i in range(2, n + 1):
            if (chs[i - 2] != '0') and int(chs[i - 2 : i]) < 26:
                dp[i] = dp[i - 2] + dp[i - 1]
            else:
                dp[i] = dp[i - 1]
        
        return dp[n]


    def crack_number_2(self, ciphertext):
        """
        crack_number_1中只使用dp中最近的两个值,因此可以使用变量代替
        """
        chs = str(ciphertext)
        a, b = 1, 1
        for i in range(2, len(chs) + 1):
            tmp = b
            if (chs[i - 2] != '0') and int(chs[i - 2 : i]) < 26:
                b = b + a
            a = tmp

        return b

def main():
    ciphertext = 216612
    sln = Solution()
    res = sln.crack_number_2(ciphertext)
    print(res)


if __name__ == "__main__":
    main()