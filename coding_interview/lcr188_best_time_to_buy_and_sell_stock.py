"""
https://leetcode.cn/problems/gu-piao-de-zui-da-li-run-lcof/?envType=study-plan-v2&envId=coding-interviews

https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/
"""

from typing import List


class Solution:
    def bestTiming(self, prices: List[int]) -> int:
        res = 0
        if not prices:
            return res
        
        min_val = prices[0]
        for i in range(1, len(prices)):
            res = max(res, prices[i] - min_val)
            min_val = min(min_val, prices[i])
        
        return res


def main():
    prices = [3, 6, 2, 9, 8, 5]
    sln = Solution()
    res = sln.bestTiming(prices)
    print(res)


if __name__ == "__main__":
    main()
