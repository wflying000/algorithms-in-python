"""
https://leetcode.cn/problems/coin-change
"""

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for j in coins:
                if j <= i:
                    dp[i] = min(dp[i], dp[i - j] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1


def main():
    sln = Solution()
    coins = [1, 2, 5]
    amount = 11
    res = sln.coinChange(coins, amount)
    print(res)


if __name__ == "__main__":
    main()