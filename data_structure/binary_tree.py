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

    @staticmethod
    def print_tree(root):
        """Pretty-print the binary tree as a top-down ASCII diagram.

        Branches are drawn with ``/`` and ``\\`` (an underscore bridges a parent
        to a subtree that starts farther away). For ``[1, 2, 3]``::

             1
            / \\
            2 3
        """
        if root is None:
            print("None")
            return ["None"]

        def _build(node):
            if node is None:
                return [], 0, 0, 0
            label = str(node.val)
            if node.left is None and node.right is None:
                return [label], len(label), 1, len(label) // 2
            if node.right is None:
                left, width, height, center = _build(node.left)
                gap = len(label)
                first = (center + 1) * " " + (width - center - 1) * "_" + label
                second = center * " " + "/" + (width - center - 1 + gap) * " "
                shifted = [row + gap * " " for row in left]
                return [first, second] + shifted, width + gap, height + 2, width + gap // 2
            if node.left is None:
                right, width, height, center = _build(node.right)
                gap = len(label)
                first = label + center * "_" + (width - center) * " "
                second = (gap + center) * " " + "\\" + (width - center - 1) * " "
                shifted = [gap * " " + row for row in right]
                return [first, second] + shifted, width + gap, height + 2, gap // 2
            left, lwidth, lheight, lcenter = _build(node.left)
            right, rwidth, rheight, rcenter = _build(node.right)
            gap = len(label)
            first = (lcenter + 1) * " " + (lwidth - lcenter - 1) * "_" + label + rcenter * "_" + (rwidth - rcenter) * " "
            second = lcenter * " " + "/" + (lwidth - lcenter - 1 + gap + rcenter) * " " + "\\" + (rwidth - rcenter - 1) * " "
            if lheight < rheight:
                left += [lwidth * " "] * (rheight - lheight)
            elif rheight < lheight:
                right += [rwidth * " "] * (lheight - rheight)
            zipped = [a + gap * " " + b for a, b in zip(left, right)]
            return [first, second] + zipped, lwidth + rwidth + gap, max(lheight, rheight) + 2, lwidth + gap // 2

        lines, *_ = _build(root)
        lines = [line.rstrip() for line in lines]
        for line in lines:
            print(line)
        return lines
