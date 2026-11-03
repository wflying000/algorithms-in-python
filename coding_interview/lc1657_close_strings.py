"""
https://leetcode.cn/problems/determine-if-two-strings-are-close
"""

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if word1 == word2:
            return True
        if len(word1) != len(word2):
            return False
        counts1 = {}
        for c in word1:
            counts1[c] = counts1.get(c, 0) + 1
        counts2 = {}
        for c in word2:
            counts2[c] = counts2.get(c, 0) + 1
        
        if set(counts1.keys()) != set(counts2.keys()):
            return False 
        
        return sorted(counts1.values()) == sorted(counts2.values())


def main():
    sln = Solution()
    word1 = "cabbba"
    word2 = "abbccc"
    res = sln.closeStrings(word1, word2)
    print(res)


if __name__ == "__main__":
    main()