"""
https://leetcode.cn/problems/li-wu-de-zui-da-jie-zhi-lcof/description/?envType=study-plan-v2&envId=coding-interviews

"""

from typing import List

class Solution:
    def jewelleryValue(self, frame: List[List[int]]) -> int:
        if not frame:
            return 0
        m = len(frame)
        n = len(frame[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = frame[0][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + frame[0][j]
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + frame[i][0]
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + frame[i][j]
        
        return dp[m - 1][n - 1]


def main():
    frame = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    sln = Solution()
    res = sln.jewelleryValue(frame)
    print(res)

if __name__ == "__main__":
    main()