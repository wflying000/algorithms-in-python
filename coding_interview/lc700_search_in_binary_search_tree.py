"""
https://leetcode.cn/problems/search-in-a-binary-search-tree
"""

from data_structure.binary_tree import TreeNode


class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        while root:
            if val < root.val:
                root = root.left 
            elif val > root.val:
                root = root.right
            else:
                return root
        return None


def main():
    sln = Solution()
    nums = [4, 2, 7, 1, 3]
    root = TreeNode.from_list(nums)
    val = 2
    res = sln.searchBST(root, val)
    print(res.val if res else None)


if __name__ == "__main__":
    main()