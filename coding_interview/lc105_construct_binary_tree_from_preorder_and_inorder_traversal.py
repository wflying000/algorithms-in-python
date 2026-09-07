"""
https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal
"""

from typing import List, Optional

from data_structure.binary_tree import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        val2idx = {x: idx for idx, x in enumerate(inorder)}
        n = len(preorder)

        return self.build_tree(preorder, 0, n - 1, inorder, 0, n - 1, val2idx)
    
    def build_tree(self, preorder, pl, pr, inorder, il, ir, val2idx):
        if pl > pr:
            return None
        if pl == pr:
            return TreeNode(preorder[pl])
        
        root = TreeNode(preorder[pl])
        idx = val2idx[preorder[pl]]
        num_left = idx - il 
        root.left = self.build_tree(preorder, pl + 1, pl + num_left, inorder, il, idx - 1, val2idx)
        root.right = self.build_tree(preorder, pl + num_left + 1, pr, inorder, idx + 1, ir, val2idx)

        return root


def main():
    sln = Solution()
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    root = sln.buildTree(preorder, inorder)
    TreeNode.print_tree(root)


if __name__ == "__main__":
    main()