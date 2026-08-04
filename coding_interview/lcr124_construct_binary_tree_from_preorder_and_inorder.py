"""
https://leetcode.cn/problems/zhong-jian-er-cha-shu-lcof/description/?envType=study-plan-v2&envId=coding-interviews

https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
"""

from collections import deque
from typing import List, Optional

from data_structure.binary_tree import TreeNode

class Solution:
    def deduceTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        val2index = {}
        for idx, val in enumerate(inorder):
            val2index[val] = idx
        
        n = len(preorder)
        return self.construct(preorder, inorder, val2index, 0, n - 1, 0, n - 1)
        
    
    def construct(self, preorder, inorder, val2index, pre_start, pre_end, in_start, in_end):
        if pre_start > pre_end or in_start > in_end:
            return None

        if pre_start == pre_end or in_start == in_end:
            return TreeNode(preorder[pre_start])
        
        val = preorder[pre_start]
        idx = val2index[val]
        root = TreeNode(val)

        num_left = idx - in_start
        new_pre_end = pre_start + num_left
        root.left = self.construct(preorder, inorder, val2index, pre_start + 1, new_pre_end, in_start, idx - 1)
        root.right = self.construct(preorder, inorder, val2index, new_pre_end + 1, pre_end, idx + 1, in_end)

        return root


def main():
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    sln = Solution()
    root = sln.deduceTree(preorder, inorder)
    TreeNode.print_tree(root)


if __name__ == "__main__":
    main()