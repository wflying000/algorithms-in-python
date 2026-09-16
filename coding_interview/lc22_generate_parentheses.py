"""
https://leetcode.cn/problems/generate-parentheses
"""

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        
        res = []
        self.backtrack(n, res, [], 0, 0)
        return res

    
    def backtrack(self, n, res, buffer, left, right):
        if len(buffer) == 2 * n:
            res.append(''.join(buffer))
            return
        
        if left < n:
            buffer.append('(')
            self.backtrack(n, res, buffer, left + 1, right)
            buffer.pop()
        
        if right < left:
            buffer.append(')')
            self.backtrack(n, res, buffer, left, right + 1)
            buffer.pop()


def main():
    sln = Solution()
    n = 3
    res = sln.generateParenthesis(n)
    print(res)


if __name__ == "__main__":
    main()