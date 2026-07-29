"""
https://leetcode.cn/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/?envType=study-plan-v2&envId=coding-interviews
"""

from collections import deque
from typing import List, Optional

from data_structure.binary_tree import TreeNode


class Solution:
    def decorateRecord(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        res = []
        left_to_right = True
        while queue:
            size = len(queue)
            cur = []
            for _ in range(size):
                node = queue.popleft()
                cur.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if not left_to_right:
                cur = cur[::-1]
            res.append(cur)
            left_to_right = not left_to_right
        return res


def main():
    values = [8, 17, 21, 18, None, None, 6]
    root = TreeNode.from_list(values)
    TreeNode.print_tree(root)
    sln = Solution()
    res = sln.decorateRecord(root)
    print(res)


if __name__ == "__main__":
    main()