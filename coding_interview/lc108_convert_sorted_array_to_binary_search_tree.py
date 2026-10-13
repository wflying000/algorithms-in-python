"""
https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree
"""

from typing import List, Optional

from data_structure.binary_tree import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        return self.build_search_tree(nums, 0, len(nums) - 1)
        
    def build_search_tree(self, nums, left, right):
        if left > right:
            return None
        if left == right:
            return TreeNode(val=nums[left])
        
        mid = (right - left) // 2 + left

        root = TreeNode(val=nums[mid])
        root.left = self.build_search_tree(nums, left, mid - 1)
        root.right = self.build_search_tree(nums, mid + 1, right)
        return root


def main():
    sln = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7]
    root = sln.sortedArrayToBST(nums)
    TreeNode.print_tree(root)


if __name__ == "__main__":
    main()