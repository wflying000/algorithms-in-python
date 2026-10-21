"""
https://leetcode.cn/problems/reverse-vowels-of-a-string
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        chs = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and s[i] not in vowels:
                i += 1
            while i < j and s[j] not in vowels:
                j -= 1
            chs[i], chs[j] = chs[j], chs[i]
            i += 1
            j -= 1
        return ''.join(chs)


def main():
    sln = Solution()
    s = "IceCreAm"
    res = sln.reverseVowels(s)
    print(res)


if __name__ == "__main__":
    main()