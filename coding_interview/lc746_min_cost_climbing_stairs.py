"""
https://leetcode.cn/problems/min-cost-climbing-stairs/
"""


class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        a, b, n = 0, 0, len(cost)
        for i in range(2, n + 1):
            c = min(a + cost[i - 2], b + cost[i - 1])
            a = b
            b = c
        return c


def main():
    sln = Solution()
    cost = [1,100,1,1,1,100,1,1,100,1]
    res = sln.minCostClimbingStairs(cost)
    print(res)

if __name__ == "__main__":
    main()