"""
https://leetcode.cn/problems/delete-the-middle-node-of-a-linked-list/
"""

from typing import Optional

from data_structure.linked_list import ListNode


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        slow, fast, pre = head, head, head 
        while fast and fast.next:
            pre = slow 
            slow = slow.next
            fast = fast.next.next 
        pre.next = pre.next.next
        return head


def main():
    sln = Solution()
    nums = [1, 3, 4, 7, 1, 2, 6]
    head = ListNode.from_list(nums)
    ListNode.print_list(head)
    res = sln.deleteMiddle(head)
    ListNode.print_list(res)


if __name__ == "__main__":
    main()
