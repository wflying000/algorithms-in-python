"""
https://leetcode.cn/problems/zheng-ze-biao-da-shi-pi-pei-lcof/description/?envType=study-plan-v2&envId=coding-interviews

https://leetcode.cn/problems/regular-expression-matching/
"""

class Solution:
    def articleMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
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
