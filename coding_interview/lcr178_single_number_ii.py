"""
https://leetcode.cn/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-ii-lcof/?envType=study-plan-v2&envId=coding-interviews
"""

from typing import List

class Solution:
    def trainingPlan(self, actions: List[int]) -> int:
        res = 0
        for i in range(32):
            num = 0
            for x in actions:
                num += (x >> i) & 1
            num = num % 3
            if num != 0:
                num = num << i
            res = res | num 
        
        return res 


def main():
    nums = [5, 7, 5, 5]
    sln = Solution()
    res = sln.trainingPlan(nums)
    print(res)


if __name__ == "__main__":
    main()