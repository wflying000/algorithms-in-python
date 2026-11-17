"""
https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii
"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        a, b = 0, -prices[0]
        for i in range(1, n):
            ta = max(a, b + prices[i])
            tb = max(b, a - prices[i])
            a, b = ta, tb 
        return a

    def maxProfit_1(self, prices: list[int]) -> int:
        n = len(prices)
        dp = [[0, 0] for _ in range(n)]
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        
        return dp[n - 1][0]

def main():
    sln = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    res = sln.maxProfit(prices)
    print(res)


if __name__ == "__main__":
    main()