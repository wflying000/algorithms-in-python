"""
https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/
"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        res = 0
        pre = prices[0]
        for i in range(1, len(prices)):
            res = max(res, prices[i] - pre)
            pre = min(pre, prices[i])
        
        return res


def main():
    sln = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    res = sln.maxProfit(prices)
    print(res)

if __name__ == "__main__":
    main()