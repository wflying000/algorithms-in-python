"""
https://leetcode.cn/problems/zheng-ze-biao-da-shi-pi-pei-lcof/description/?envType=study-plan-v2&envId=coding-interviews

https://leetcode.cn/problems/regular-expression-matching/
"""

class Solution:
    def articleMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        # dp[i][j] 的意义定义为p[0 ... j-1]是否能匹配s[0 ... i - 1]
        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][0] = True

        for i in range(2, n + 1, 2):
            if p[i - 1] == "*":
                dp[0][i] = True
            else:
                break
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                sc = s[i - 1]
                pc = p[j - 1]

                # p[j - 1]为'*'时，p[j - 2]可以使用0次和至少使用1次
                # 如果p[j - 2]使用零次等价与判断p[0 .. j-3]是否可以与s[0 .. i - 1]匹配
                # 如果p[j - 2]至少使用1次，需要保证p[j-2]能匹配s[i-1]即p[j-2]==s[i-1]或p[j-2]=='.', 然后判断p[0..j-1]能否匹配s[0..i-2]
                if pc == "*":
                    dp[i][j] = dp[i][j - 2]
                    if p[j - 2] == sc or p[j - 2] == '.' :
                        dp[i][j] = dp[i][j] or dp[i - 1][j]

                    
                elif pc == sc or pc == '.':
                    dp[i][j] = dp[i - 1][j - 1]
        
        return dp[m][n]


def main():
    s = "abcc"
    p = "a.c*"
    sln = Solution()
    res = sln.articleMatch(s, p)
    print(res)


if __name__ == "__main__":
    main()
