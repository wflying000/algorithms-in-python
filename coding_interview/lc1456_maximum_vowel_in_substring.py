"""
https://leetcode.cn/problems/maximum-number-of-vowels-in-a-substring-of-given-length
"""

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel_set = {'a', 'e', 'i', 'o', 'u'}
        cnt = 0
        for i in range(k):
            if s[i] in vowel_set:
                cnt += 1
        res = cnt
        for i in range(k, len(s)):
            if s[i] in vowel_set:
                cnt += 1
            if s[i - k] in vowel_set:
                cnt -= 1
            res = max(res, cnt)
        return res


def main():
    sln = Solution()
    s = "abciiidef"
    k = 3
    res = sln.maxVowels(s, k)
    print(res)


if __name__ == "__main__":
    main()
    
