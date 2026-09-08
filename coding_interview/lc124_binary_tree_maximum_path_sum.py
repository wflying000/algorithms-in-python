"""
https://leetcode.cn/problems/binary-tree-maximum-path-sum
"""

from typing import Optional

from data_structure.binary_tree import TreeNode


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.res = float("-inf")
        self.dfs(root)
        return self.res

    
    def dfs(self, root):
        if not root:
            return 0
        
        left = max(self.dfs(root.left), 0)
        right = max(self.dfs(root.right), 0)

        s = root.val + left + right
        self.res = max(self.res, s)

        return root.val + max(left, right)


def main():
    sln = Solution()
    nums = [-10, 9, 20, None, None, 15, 7]
    root = TreeNode.from_list(nums)
    TreeNode.print_tree(root)

    res = sln.maxPathSum(root)
    print(res)


if __name__ == "__main__":
    main()