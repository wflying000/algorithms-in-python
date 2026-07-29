from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, values):
        """Construct a binary tree from its level-order traversal.

        ``values`` follows LeetCode's convention where ``None`` denotes an
        absent node. For example, ``[1, None, 3, 4]`` produces a root ``1``
        with an empty left child, a right child ``3``, and ``3`` itself has a
        left child ``4``.
        """
        if not values or values[0] is None:
            return None
        root = cls(values[0])
        queue = deque([root])
        index = 1
        length = len(values)
        while queue and index < length:
            node = queue.popleft()
            if index < length:
                value = values[index]
                index += 1
                if value is not None:
                    node.left = cls(value)
                    queue.append(node.left)
            if index < length:
                value = values[index]
                index += 1
                if value is not None:
                    node.right = cls(value)
                    queue.append(node.right)
        return root
