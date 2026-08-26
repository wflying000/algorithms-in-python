"""
https://leetcode.cn/problems/linked-list-cycle
"""

from typing import Optional

from data_structure.linked_list import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


def main():
    sln = Solution()

    nums = [1, 2, 3, 4]
    head, nodes = ListNode.from_list(nums, with_nodes=True)
    nodes[-1].next = nodes[1]
    res = sln.hasCycle(head)
    print(res)

    nums = [1, 2, 3]
    head = ListNode.from_list(nums)
    res = sln.hasCycle(head)
    print(res)


if __name__ == "__main__":
    main()
