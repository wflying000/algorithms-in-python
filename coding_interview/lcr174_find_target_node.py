"""
https://leetcode.cn/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/description/?envType=study-plan-v2&envId=coding-interviews
"""

from collections import deque
from typing import List, Optional

from data_structure.binary_tree import TreeNode


class Solution:
    def findTargetNode(self, root: Optional[TreeNode], cnt: int) -> int:
        if not root:
            return None
        
        stack = deque()
        while stack or root:
            while root:
                stack.append(root)
                root = root.right
            
            root = stack.pop()
            cnt -= 1
            if cnt == 0:
                return root.val
            root = root.left
        
        return None


def main():
    values = [10, 5, 15, 2, 7, None, 20, 1, None, 6, 8]
    cnt = 4
    root = TreeNode.from_list(values)
    TreeNode.print_tree(root)

    sln = Solution()
    res = sln.findTargetNode(root, cnt)
    print(res)


if __name__ == "__main__":
    main()