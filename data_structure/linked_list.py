
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, values, with_nodes=False):
        """Construct a linked list from ``values`` and return its head node.

        By default returns only the ``head``. When ``with_nodes`` is true,
        returns a tuple ``(head, nodes)`` where ``nodes`` is positionally
        aligned with ``values``: ``nodes[i]`` is the ``ListNode`` created for
        ``values[i]``.
        """
        head = None
        tail = None
        nodes = [None] * len(values)

        for index, value in enumerate(values):
            node = cls(value)
            nodes[index] = node
            if head is None:
                head = node
            else:
                tail.next = node
            tail = node

        return (head, nodes) if with_nodes else head

    @staticmethod
    def print_list(head):
        """Print a linked list's values in Python list format."""
        values = []
        current = head
        while current is not None:
            values.append(current.val)
            current = current.next

        print(values)
        return values
