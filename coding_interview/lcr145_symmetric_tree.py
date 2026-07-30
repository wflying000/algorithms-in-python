"""
https://leetcode.cn/problems/dui-cheng-de-er-cha-shu-lcof/description/?envType=study-plan-v2&envId=coding-interviews

https://leetcode.cn/problems/symmetric-tree/
"""

from collections import deque
from typing import List, Optional

from data_structure.binary_tree import TreeNode

class Solution:
    def checkSymmetricTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.check(root.left, root.right)

    def check(self, root1, root2):
        if (not root1) and (not root2):
            return True
        if (not root1) or (not root2):
            return False
        
        return (root1.val == root2.val) and self.check(root1.left, root2.right) and self.check(root1.right, root2.left)


def main():
    values = [1, 2, 2, None, 3, None, 3]
    root = TreeNode.from_list(values)
    TreeNode.print_tree(root)

    sln = Solution()
    print(sln.checkSymmetricTree(root))


if __name__ == "__main__":
    main()