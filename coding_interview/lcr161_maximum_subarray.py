"""
https://leetcode.cn/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/description/?envType=study-plan-v2&envId=coding-interviews

https://leetcode.cn/problems/maximum-subarray/
"""

from typing import List

class Solution:
    def maxSales(self, sales: List[int]) -> int:
        if not sales:
            return 0
        res = sales[0]
        s = sales[0]
        for i in range(1, len(sales)):
            s = max(s + sales[i], sales[i])
            res = max(res, s)
        
        return res


def main():
    sales = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    sln = Solution()
    res = sln.maxSales(sales)
    print(res)

if __name__ == "__main__":
    main()