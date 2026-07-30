"""
https://leetcode.cn/problems/er-cha-shu-de-jing-xiang-lcof/description/?envType=study-plan-v2&envId=coding-interviews

https://leetcode.cn/problems/invert-binary-tree/description/
"""

from collections import deque
from typing import List, Optional

from data_structure.binary_tree import TreeNode

class Solution:
    def flipTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        root.left, root.right = root.right, root.left

        self.flipTree(root.left)
        self.flipTree(root.right)

        return root


def main():
    values = [5, 7, 9, 8, 3, 2, 4]
    root = TreeNode.from_list(values)
    TreeNode.print_tree(root)

    sln = Solution()
    root = sln.flipTree(root)
    TreeNode.print_tree(root)

if __name__ == "__main__":
    main()
