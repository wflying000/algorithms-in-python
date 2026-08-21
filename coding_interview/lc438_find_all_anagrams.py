"""
https://leetcode.cn/problems/find-all-anagrams-in-a-string
"""

from typing import List


class Solution:

    def findAnagrams(self, s: str, p: str) -> List[int]:

        return self.findAnagrams_2(s, p)

    def findAnagrams_2(self, s: str, p: str) -> List[int]:
        m, n = len(s), len(p)
        if m < n:
            return []
        res = []
        diff = [0] * 26
        base_num = ord('a')
        for i in range(n):
            diff[ord(s[i]) - base_num] += 1
            diff[ord(p[i]) - base_num] -= 1
        
        count = sum([x != 0 for x in diff])
        if count == 0:
            res.append(0)
        
        for i in range(1, m - n + 1):

            if diff[ord(s[i - 1]) - base_num] == 1:
                count -= 1
            elif diff[ord(s[i - 1]) - base_num] == 0:
                count += 1
            
            diff[ord(s[i - 1]) - base_num] -= 1
            
            if diff[ord(s[i + n - 1]) - base_num] == -1:
                count -= 1
            if diff[ord(s[i + n - 1]) - base_num] == 0:
                count += 1
            
            diff[ord(s[i + n - 1]) - base_num] += 1

            if count == 0:
                res.append(i)

        return res

    def findAnagrams_2(self, s: str, p: str) -> List[int]:
        m, n = len(s), len(p)
        if m < n:
            return []
        res = []
        diff = [0] * 26
        base_num = ord('a')
        for i in range(n):
            diff[ord(s[i]) - base_num] += 1
            diff[ord(p[i]) - base_num] -= 1
        
        count = sum([x != 0 for x in diff])
        if count == 0:
            res.append(0)
        
        for i in range(1, m - n + 1):

            if diff[ord(s[i - 1]) - base_num] == 1:
                count -= 1
            elif diff[ord(s[i - 1]) - base_num] == 0:
                count += 1
            
            diff[ord(s[i - 1]) - base_num] -= 1
            
            if diff[ord(s[i + n - 1]) - base_num] == -1:
                count -= 1
            if diff[ord(s[i + n - 1]) - base_num] == 0:
                count += 1
            
            diff[ord(s[i + n - 1]) - base_num] += 1

            if count == 0:
                res.append(i)

        return res

    def findAnagrams_1(self, s: str, p: str) -> List[int]:
        m, n = len(s), len(p)
        if m < n:
            return []
        reference = [0] * 26
        for ch in p:
            reference[ord(ch) - ord('a')] += 1
        current = [0] * 26
        for i in range(n):
            current[ord(s[i]) - ord('a')] += 1
        res = []
        if current == reference:
            res.append(0)
        
        for i in range(1, m - n + 1):
            current[ord(s[i - 1]) - ord('a')] -= 1
            current[ord(s[i + n - 1]) - ord('a')] += 1
            if current == reference:
                res.append(i)
        
        return res


def main():
    sln = Solution()
    s = "cbaebabacd"
    p = "abc"
    res = sln.findAnagrams(s, p)
    print(res)


if __name__ == "__main__":
    main()