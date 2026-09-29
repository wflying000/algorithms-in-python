"""
https://leetcode.cn/problems/daily-temperatures
"""

from collections import deque


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        if not temperatures:
            return []
        res = [0] * len(temperatures)
        stack = deque()
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                j = stack.pop()
                res[j] = i - j
            stack.append(i)
        
        return res


def main():
    sln = Solution()
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    res = sln.dailyTemperatures(temperatures)
    print(res)


if __name__ == "__main__":
    main()