"""
https://leetcode.cn/problems/er-cha-shu-de-shen-du-lcof/?envType=study-plan-v2&envId=coding-interviews

https://leetcode.cn/problems/maximum-depth-of-binary-tree/
"""

from collections import deque
from typing import List, Optional

from data_structure.binary_tree import TreeNode


class Solution:
    def calculateDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max(self.calculateDepth(root.left), self.calculateDepth(root.right))


def main():
    values = [1, 2, 2, 3, None, None, 5, 4, None, None, 4]
    root = TreeNode.from_list(values)
    TreeNode.print_tree(root)
    
    sln = Solution()
    res = sln.calculateDepth(root)
    print(res)


if __name__ == "__main__":
    main()