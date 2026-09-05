"""
https://leetcode.cn/problems/kth-smallest-element-in-a-bst
"""

from typing import Optional
from collections import deque

from data_structure.binary_tree import TreeNode


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = deque()
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
        
        return None


def main():
    sln = Solution()
    nums = [3, 1, 4, None, 2]
    root = TreeNode.from_list(nums)
    k = 3
    res = sln.kthSmallest(root, k)
    print(res)


if __name__ == "__main__":
    main()