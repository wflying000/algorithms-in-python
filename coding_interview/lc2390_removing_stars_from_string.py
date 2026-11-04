"""
https://leetcode.cn/problems/removing-stars-from-a-string
"""

class Solution:
    def removeStars(self, s: str) -> str:
        chs = []
        for x in s:
            if x != '*':
                chs.append(x)
            else:
                chs.pop()
        return "".join(chs)


def main():
    sln = Solution()
    s = "leet**cod*e"
    res = sln.removeStars(s)
    print(res)


if __name__ == "__main__":
    main()