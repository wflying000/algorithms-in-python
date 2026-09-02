"""
https://leetcode.cn/problems/diameter-of-binary-tree
"""

from typing import Optional

from data_structure.binary_tree import TreeNode


class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.get_max_depth(root)
        return self.res - 1 # 边数等于节点数减一

    def get_max_depth(self, root):
        if not root:
            return 0

        left = self.get_max_depth(root.left)
        right = self.get_max_depth(root.right)
        self.res = max(self.res, left + right + 1)

        return max(left, right) + 1 # 返回当前节点的最大深度

    
def main():
    sln = Solution()
    nums = [1, 2, 3, 4, 5]
    root = TreeNode.from_list(nums)
    TreeNode.print_tree(root)

    res = sln.diameterOfBinaryTree(root)
    print(res)


if __name__ == "__main__":
    main()