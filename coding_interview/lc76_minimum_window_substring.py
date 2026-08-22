"""
https://leetcode.cn/problems/minimum-window-substring
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        ch2cnt = {}
        for ch in t:
            ch2cnt[ch] = ch2cnt.get(ch, 0) + 1
        i = 0
        count = len(t)
        left, right = -1, len(s)
        for j, ch in enumerate(s):
            if ch not in ch2cnt:
                continue
            if ch2cnt[ch] > 0:
                count -= 1
            ch2cnt[ch] -= 1

            while i <= j and count == 0:
                if j - i < right - left:
                    left, right = i, j
                if s[i] in ch2cnt:
                    ch2cnt[s[i]] += 1
                    if ch2cnt[s[i]] > 0:
                        count += 1
                i += 1
        
        return "" if left == -1 else s[left : right + 1]


def main():
    sln = Solution()
    s = "ADOBECODEBANC"
    t = "ABC"
    res = sln.minWindow(s, t)
    print(res)


if __name__ == "__main__":
    main()