"""
https://leetcode.cn/problems/flatten-binary-tree-to-linked-list
"""

from typing import Optional
from collections import deque

from data_structure.binary_tree import TreeNode


class Solution:

    def flatten(self, root: Optional[TreeNode]) -> None:
        
        # self.flatten_1(root)
        self.flatten_2(root)

    def flatten_2(self, root):
        if not root:
            return None
        stack = deque()
        stack.append(root)
        pre = None
        while stack:
            cur = stack.pop()
            if pre is not None:
                pre.right = cur
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
            cur.left = None
            pre = cur 

    def flatten_1(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        
        pre = None
        stack = deque()
        while root or stack:
            while root:
                if pre is not None:
                    pre.right = root
                pre = root
                if root.right:
                    stack.append(root.right)
                left = root.left
                root.left = None
                root = left 
            if stack:
                root = stack.pop()


def main():
    sln = Solution()
    nums = [1, 2, 5, 3, 4, None, 6]
    root = TreeNode.from_list(nums)
    sln.flatten(root)
    TreeNode.print_tree(root)


if __name__ == "__main__":
    main()