"""
https://leetcode.cn/problems/longest-substring-without-repeating-characters
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ch2idx = {}
        pre, res = -1, 0
        for idx, ch in enumerate(s):
            pre = max(pre, ch2idx.get(ch, -1))
            res = max(res, idx - pre)
            ch2idx[ch] = idx
        
        return res


def main():
    sln = Solution()
    s = "pwwkew"
    res = sln.lengthOfLongestSubstring(s)
    print(res)


if __name__ == "__main__":
    main()
