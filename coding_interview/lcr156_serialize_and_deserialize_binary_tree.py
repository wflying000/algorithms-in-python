"""
https://leetcode.cn/problems/xu-lie-hua-er-cha-shu-lcof/description/?envType=study-plan-v2&envId=coding-interviews

https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/
"""

from collections import deque
from typing import List, Optional

from data_structure.binary_tree import TreeNode


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        values = []
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node:
                values.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                values.append("#")
        return "_".join(values)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        values = data.split("_")
        root = TreeNode(int(values[0]))
        queue = deque()
        queue.append(root)
        i = 1
        while queue:
            node = queue.popleft()
            if values[i] != "#":
                node.left = TreeNode(int(values[i]))
                queue.append(node.left)
            i += 1
            if values[i] != "#":
                node.right = TreeNode(int(values[i]))
                queue.append(node.right)
            i += 1
        return root

def main():
    values = [1, 2, 3, None, None, 4, 5]
    root = TreeNode.from_list(values)
    TreeNode.print_tree(root)

    codec = Codec()
    data = codec.serialize(root)
    print(data)
    new_root = codec.deserialize(data)
    TreeNode.print_tree(new_root)


if __name__ == "__main__":
    main()