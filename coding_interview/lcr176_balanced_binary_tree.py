"""
https://leetcode.cn/problems/ping-heng-er-cha-shu-lcof/description/?envType=study-plan-v2&envId=coding-interviews

https://leetcode.cn/problems/balanced-binary-tree/
"""

from collections import deque
from typing import List, Optional

from data_structure.binary_tree import TreeNode


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # return self.is_balanced_1(root)

        return self.is_balanced_2(root)[1]

    def is_balanced_1(self, root):
        """
        自顶向下, 每个节点都需要重新计算深度, 计算量大
        """
        if not root:
            return True

        left = self.max_depth(root.left)
        right = self.max_depth(root.right)

        return abs(left - right) <= 1 and self.is_balanced_1(root.left) and self.is_balanced_1(root.right)
    
    def max_depth(self, root):
        if not root:
            return 0
        return 1 + max(self.max_depth(root.left), self.max_depth(root.right))
    

    def is_balanced_2(self, root):
        """
        自底向上, 每个节点向上提供depth和is_balanced信息, 减少重复计算
        """
        if not root:
            return 0, True
        
        left_depth, left_balanced = self.is_balanced_2(root.left)
        if not left_balanced:
            return -1, False
        
        right_depth, right_balanced = self.is_balanced_2(root.right)
        if not right_balanced:
            return -1, False

        if abs(left_depth - right_depth) > 1:
            return -1, False

        return 1 + max(left_depth, right_depth), True


def main():
    values = [1, 2, 2, 3, 3, None, None, 4, 4]
    root = TreeNode.from_list(values)
    TreeNode.print_tree(root)

    sln = Solution()
    res = sln.isBalanced(root)
    print(res)



if __name__ == "__main__":
    main()