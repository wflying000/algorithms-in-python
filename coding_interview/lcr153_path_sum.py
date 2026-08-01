"""
https://leetcode.cn/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/description/?envType=study-plan-v2&envId=coding-interviews

https://leetcode.cn/problems/path-sum-ii/description/
"""

from collections import deque
from typing import List, Optional

from data_structure.binary_tree import TreeNode


class Solution:
    def pathTarget(self, root: Optional[TreeNode], target: int) -> List[List[int]]:
        vals, res = [], []
        self.process(root, target, vals, res)
        return res

    def process(self, root, target, vals, res):
        if not root:
            return
        vals.append(root.val)
        target -= root.val
        if (not root.left) and (not root.right) and target == 0:
            res.append([x for x in vals])
            vals.pop()
            return
        
        self.process(root.left, target, vals, res)
        self.process(root.right, target, vals, res)
        vals.pop()

        
def main():
    values = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
    target = 22
    root = TreeNode.from_list(values)
    TreeNode.print_tree(root)
    sln = Solution()
    res = sln.pathTarget(root, target)
    print(res)


if __name__ == "__main__":
    main()