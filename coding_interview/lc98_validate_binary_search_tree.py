"""
https://leetcode.cn/problems/validate-binary-search-tree
"""

from typing import Optional
from collections import deque

from data_structure.binary_tree import TreeNode


class Solution:

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # return self.judge_inorder(root)

        return self.judge_recur(root, None, None)

    def judge_recur(self, root, lower, upper):
        if not root:
            return True
        
        if lower is not None and root.val <= lower:
            return False
        if upper is not None and root.val >= upper:
            return False
        
        if not self.judge_recur(root.left, lower, root.val):
            return False
            
        if not self.judge_recur(root.right, root.val, upper):
            return False

        return True

        


    def judge_inorder(self, root):
        stack = deque()
        pre = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pre is not None:
                if pre.val >= root.val:
                    return False
            pre = root
            root = root.right
        
        return True


def main():
    sln = Solution()
    nums = [0, None, -1]
    root = TreeNode.from_list(nums)
    TreeNode.print_tree(root)

    res = sln.isValidBST(root)
    print(res)


if __name__ == "__main__":
    main()
    