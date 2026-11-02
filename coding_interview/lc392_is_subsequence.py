"""
https://leetcode.cn/problems/is-subsequence
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j, m, n = 0, 0, len(s), len(t)
        while i < m and j < n:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == m


def main():
    sln = Solution()
    s = "abc"
    t = "ahbgdc"
    res = sln.isSubsequence(s, t)
    print(res)


if __name__ == "__main__":
    main()