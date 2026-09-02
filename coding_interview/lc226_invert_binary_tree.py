"""
https://leetcode.cn/problems/invert-binary-tree
"""

from typing import Optional

from data_structure.binary_tree import TreeNode


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root



def main():
    sln = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7]
    root = TreeNode.from_list(nums)
    TreeNode.print_tree(root)

    root = sln.invertTree(root)
    TreeNode.print_tree(root)


if __name__ == "__main__":
    main()
