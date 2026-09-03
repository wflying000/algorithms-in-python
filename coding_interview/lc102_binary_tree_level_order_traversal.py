"""
https://leetcode.cn/problems/binary-tree-level-order-traversal
"""

from collections import deque
from typing import Optional, List

from data_structure.binary_tree import TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = deque()
        queue.append(root)
        while queue:
            size = len(queue)
            tmp = []
            for _ in range(size):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            res.append(tmp)
        return res

def main():
    sln = Solution()
    nums = [1, 2, 3, None, None, 4, 5]
    root = TreeNode.from_list(nums)
    TreeNode.print_tree(root)
    res = sln.levelOrder(root)
    print(res)


if __name__ == "__main__":
    main()