"""
https://leetcode.cn/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof/description/?envType=study-plan-v2&envId=coding-interviews

https://leetcode.cn/problems/binary-tree-level-order-traversal/description/
"""


from collections import deque
from typing import List, Optional

from data_structure.binary_tree import TreeNode

class Solution:
    def decorateRecord(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        res = []
        while queue:
            node = queue.popleft()
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res


def main():
    values = [8, 17, 21, 18, None, None, 6]
    root = TreeNode.from_list(values)
    sln = Solution()
    res = sln.decorateRecord(root)
    print(res)


if __name__ == "__main__":
    main()