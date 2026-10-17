"""
https://leetcode.cn/problems/longest-palindromic-substring
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        start, end = 0, 0
        for i in range(n):
            dp[i][i] = True
            if i + 1 < n and s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start, end = i, i + 1
        
        for length in range(3, n + 1):
            for i in range(n):
                j = i + length - 1
                if j >= n:
                    break
                dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]
                if dp[i][j]:
                    start, end = i, j
        
        return s[start : end + 1]


def main():
    sln = Solution()
    s = "babad"
    res = sln.longestPalindrome(s)
    print(res)


if __name__ == "__main__":
    main()