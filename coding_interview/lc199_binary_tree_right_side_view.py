"""
https://leetcode.cn/problems/binary-tree-right-side-view
"""

from typing import Optional, List
from collections import deque

from data_structure.binary_tree import TreeNode


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        res = []
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if i == size - 1:
                    res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return res


def main():
    sln = Solution()
    nums = [1, 2, 3, 4, None, None, None, 5]
    root = TreeNode.from_list(nums)
    res = sln.rightSideView(root)
    print(res)


if __name__ == "__main__":
    main()

