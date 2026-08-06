
"""
https://leetcode.cn/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/?envType=study-plan-v2&envId=coding-interviews
"""
from typing import List
from functools import cmp_to_key

class Solution:
    def crackPassword(self, password: List[int]) -> str:
        
        def compare(a, b):
            num1 = int(str(a) + str(b))
            num2 = int(str(b) + str(a))
            return num1 - num2
        
        res = sorted(password, key=cmp_to_key(compare))
        res = "".join([str(x) for x in res])
        return res


def main():
    sln = Solution()
    password = [0, 3, 30, 34, 5, 9]
    res = sln.crackPassword(password)
    print(res)


if __name__ == "__main__":
    main()