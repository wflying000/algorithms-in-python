"""
https://leetcode.cn/problems/permutations
"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        visited = [False for _ in range(len(nums))]
        res = []
        self.backtrack(nums, visited, [], res)
        return res
    
    def backtrack(self, nums, visited, buffer, res):
        if len(buffer) == len(nums):
            res.append([x for x in buffer])
            return
        for i, num in enumerate(nums):
            if not visited[i]:
                visited[i] = True
                buffer.append(num)
                self.backtrack(nums, visited, buffer, res)
                visited[i] = False
                buffer.pop()


def main():
    sln = Solution()
    nums = [1, 2, 3]
    res = sln.permute(nums)
    print(res)


if __name__ == "__main__":
    main()