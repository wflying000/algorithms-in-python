"""
https://leetcode.cn/problems/shu-de-zi-jie-gou-lcof/?envType=study-plan-v2&envId=coding-interviews
"""
from collections import deque
from typing import List, Optional

from data_structure.binary_tree import TreeNode


class Solution:
    def isSubStructure(self, A: Optional[TreeNode], B: Optional[TreeNode]) -> bool:
        if (not A) or (not B):
            return False
        return self.process(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)
    
    def process(self, A, B):
        if not B:
            return True
        if not A:
            return False        
        return (A.val == B.val) and self.process(A.left, B.left) and self.process(A.right, B.right) 


def main():
    values1 = [1, 2, 3, 4]
    root1 = TreeNode.from_list(values1)

    values2 = [3]
    root2 = TreeNode.from_list(values2)

    sln = Solution()
    res = sln.isSubStructure(root1, root2)
    print(res)


if __name__ == "__main__":
    main()
