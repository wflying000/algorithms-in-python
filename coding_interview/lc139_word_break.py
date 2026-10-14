"""
https://leetcode.cn/problems/word-break
"""

from typing import List


class Solution:

    def wordBreak(self, s, wordDict):
        return self.wordBreak_dp(s, wordDict)
    

    def wordBreak_dp(self, s, wordDict):
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break 
        return dp[n]

    def wordBreak_dfs_mem(self, s: str, wordDict: List[str]) -> bool:
        self.mem = {}
        return self.dfs(s, wordDict, 0)

    def dfs(self, s, wordDict, idx):
        if idx >= len(s):
            return True
        if idx in self.mem:
            return self.mem[idx]
        for word in wordDict:
            if s.startswith(word, idx) and self.dfs(s, wordDict, idx + len(word)):
                self.mem[idx] = True
                return True

        # 失败的后缀也必须缓存，避免其他拆分路径重复搜索。
        self.mem[idx] = False
        return False


def main():
    sln = Solution()
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    res = sln.wordBreak(s, wordDict)
    print(res)


if __name__ == "__main__":
    main()
