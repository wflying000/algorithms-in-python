"""
https://leetcode.cn/problems/combination-sum
"""

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        self.backtrack(candidates, 0, target, [], res)

        return res

    
    def backtrack(self, candidates, idx, target, buffer, res):
        if target == 0:
            res.append([x for x in buffer])
            return
        
        if idx == len(candidates):
            return

        # 选择当前索引位置的数
        if target - candidates[idx] >= 0:
            tgt = target - candidates[idx]
            buffer.append(candidates[idx])
            self.backtrack(candidates, idx, tgt, buffer, res)
            buffer.pop()
        
        # 不选择当前索引位置的数
        self.backtrack(candidates, idx + 1, target, buffer, res)


def main():
    sln = Solution()
    candidates = [2, 3, 5]
    target = 8
    res = sln.combinationSum(candidates, target)
    print(res)


if __name__ == "__main__":
    main()