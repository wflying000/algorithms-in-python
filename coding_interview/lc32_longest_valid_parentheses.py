"""
https://leetcode.cn/problems/longest-valid-parentheses
"""

from collections import deque 


class Solution:

    def longestValidParentheses(self, s: str) -> int:
        left, right = 0, 0
        n, res = len(s), 0
        for i in range(n):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                res = max(res, 2 * left)
            elif left < right:
                left, right = 0, 0
        left, right = 0, 0
        for i in range(n - 1, -1, -1):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            
            if left == right:
                res = max(res, 2 * left)
            elif left > right:
                left, right = 0, 0
        
        return res

    def longestValidParentheses_stack(self, s: str) -> int:
        stack = deque()
        stack.append(-1)
        res = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    res = max(res, i - stack[-1])
        
        return res

    def longestValidParentheses_dp(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        dp = [0] * n
        res = 0
        for i in range(1, n):
            if s[i] != ')':
                continue
            if s[i - 1] == '(':
                dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
            elif (i - dp[i - 1] > 0) and s[i - dp[i - 1] - 1] == '(' and dp[i - 1] > 0:
                dp[i] = dp[i - 1] + 2 + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] >= 2 else 0)
            res = max(res, dp[i])
        return res


def main():
    sln = Solution()
    s = ")()())"
    res = sln.longestValidParentheses(s)
    print(res)


if __name__ == "__main__":
    main()
