"""
https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree
"""

from data_structure.binary_tree import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        return self.dfs(root, p, q)
        
    def dfs(self, root, p, q):
        if not root:
            return None
        if root == p or root == q:
            return root
        left = self.dfs(root.left, p, q)
        right = self.dfs(root.right, p, q)
        if not left:
            return right
        if not right:
            return left
        return root


def main():
    sln = Solution()
    nums = [3, 5, 1, 6, 2, 0, 8, None, None, 7,4]
    root, nodes = TreeNode.from_list(nums, with_nodes=True)
    p, q = nodes[3], nodes[9]

    TreeNode.print_tree(root)
    res = sln.lowestCommonAncestor(root, p, q)
    print(res.val)


if __name__ == "__main__":
    main()