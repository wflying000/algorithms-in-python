"""
https://leetcode.cn/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/description/?envType=study-plan-v2&envId=coding-interviews

https://leetcode.cn/problems/convert-binary-search-tree-to-sorted-doubly-linked-list
"""

from collections import deque
from typing import List, Optional

from data_structure.binary_tree import TreeNode


class Solution:
    def treeToDoublyList(self, root: TreeNode) -> TreeNode:
        return self.tree_to_doubly_list_2(root)
    
    def tree_to_doubly_list_2(self, root):
        if not root:
            return None
        
        stack = deque()
        cur = root
        pre = None
        res = None

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            
            cur = stack.pop()
            if pre is None:
                pre = cur
                res = cur
            else:
                pre.right = cur
                cur.left = pre
                pre = cur

            if (not cur.right) and (not stack):
                cur.right = res
                res.left = cur
                break

            cur = cur.right

        return res               

            
            



    def tree_to_doubly_list_1(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        stack = deque()
        cur = root
        node_list = []

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            
            cur = stack.pop()
            node_list.append(cur)
            cur = cur.right
        n = len(node_list)
        for i in range(n):
            prev_index = i - 1
            next_index = (i + 1) % n 
            node_list[i].left = node_list[prev_index]
            node_list[i].right = node_list[next_index]

        return node_list[0]   



def main():
    values = [4, 2, 5, 1, 3]
    root = TreeNode.from_list(values)
    TreeNode.print_tree(root)

    sln = Solution()
    res = sln.treeToDoublyList(root)
    print(res.val)


if __name__ == "__main__":
    main()
