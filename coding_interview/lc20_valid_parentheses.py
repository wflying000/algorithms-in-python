"""
https://leetcode.cn/problems/valid-parentheses
"""

from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = deque()

        for c in s:
            if c in {'(', '[', '{'}:
                stack.append(c)
            else:
                if not stack:
                    return False
                t = stack.pop()
                if (c == ')' and t != '(') or (c == ']' and t != '[') or (c == '}' and t != '{'):
                    return False

        return not stack


def main():
    sln = Solution()
    s = "()[]{}"
    res = sln.isValid(s)
    print(res)


if __name__ == "__main__":
    main()