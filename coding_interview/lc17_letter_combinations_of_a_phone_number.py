"""
https://leetcode.cn/problems/letter-combinations-of-a-phone-number
"""

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit2alpha = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []
        self.backtrack(digits, 0, digit2alpha, [], res)

        return res

    
    def backtrack(self, digits, idx, digit2alpha, buffer, res):
        if idx == len(digits):
            res.append("".join(buffer))
            return
        
        digit = digits[idx]
        for c in digit2alpha[digit]:
            buffer.append(c)
            self.backtrack(digits, idx + 1, digit2alpha, buffer, res)
            buffer.pop()
         

def main():
    sln = Solution()
    digits = "23"
    res = sln.letterCombinations(digits)
    print(res)


if __name__ == "__main__":
    main()