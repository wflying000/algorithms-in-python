"""
https://leetcode.cn/problems/palindrome-partitioning
"""


class Solution:

    def partition(self, s: str) -> list[list[str]]:

        return self.partition_dp_backtrack(s)

    

    def partition_dp_backtrack(self, s):
        n = len(s)
        f = [[True] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                f[i][j] = (s[i] == s[j]) and f[i + 1][j - 1]
        
        res = []
        buffer = []
        
        def dfs(i):
            if i == n:
                res.append(buffer[:])
                return
            
            for j in range(i, n):
                if f[i][j]:
                    buffer.append(s[i : j + 1])
                    dfs(j + 1)
                    buffer.pop()
        
        dfs(0)

        return res



def main():
    sln = Solution()
    s = "aab"
    res = sln.partition(s)
    print(res)


if __name__ == "__main__":
    main()