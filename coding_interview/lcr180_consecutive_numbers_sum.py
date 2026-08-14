"""
https://leetcode.cn/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/description/?envType=study-plan-v2&envId=coding-interviews

"""

import math
from typing import List

class Solution:
    def fileCombination(self, target: int) -> List[List[int]]:
    
        # res = self.process_enumerate(target)
        # res = self.process_math(target)
        res = self.process_two_points(target)
        return res
    
    def process_enumerate(self, target):
        mid = (target - 1) // 2
        res = []
        for i in range(1, mid + 1):
            s = 0
            for j in range(i, target):
                s += j
                if s > target:
                    break
                elif s == target:
                    res.append(list(range(i, j + 1)))
                    break
        
        return res

    
    def process_math(self, target):
        mid = (target - 1) // 2
        res = []
        # 假设 i + (i + 1) + ... + j = target
        # (i + j) * (j - i + 1) / 2 = target
        # 整理得 j^2 + j + i - i^2 - 2t = 0
        # j = (-1 +/- sqrt(1 + 4(i^2 + 2t - i)))  / 2
        for i in range(1, mid + 1):
            delta = 1 + 4 * (i * i + 2 * target - i)
            if delta < 0:
                continue

            delta_sqrt = int(math.sqrt(delta))
            if delta_sqrt * delta_sqrt == delta and (delta_sqrt - 1) % 2 == 0:
                j = (delta_sqrt - 1) // 2
                if (i < j):
                    res.append(list(range(i, j + 1)))
        
        return res

    def process_two_points(self, target):
        i, j = 1, 2
        res = []
        while i < j:
            s = (i + j) * (j - i + 1) // 2

            if s < target:
                j += 1
            elif s > target:
                i += 1
            else:
                res.append(list(range(i, j + 1)))
                i += 1
        
        return res


def main():
    sln = Solution()
    target = 18
    res = sln.fileCombination(target)
    print(res)


if __name__ == "__main__":
    main()