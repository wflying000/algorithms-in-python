
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, values):
        """Construct a linked list from ``values`` and return its head node."""
        head = None
        tail = None

        for value in values:
            node = cls(value)
            if head is None:
                head = node
            else:
                tail.next = node
            tail = node

        return head

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
