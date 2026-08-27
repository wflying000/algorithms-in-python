"""
https://leetcode.cn/problems/remove-nth-node-from-end-of-list
"""

from typing import Optional

from data_structure.linked_list import ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        dummy = ListNode(next=head)
        p1 = head
        i = 0
        while p1 and i < n:
            p1 = p1.next
            i += 1
        p2 = dummy
        while p1:
            p1 = p1.next
            p2 = p2.next
        p2.next = p2.next.next

        return dummy.next
        

def main():
    sln = Solution()
    nums = [1, 2, 3, 4, 5]
    head = ListNode.from_list(nums)
    n = 2

    res = sln.removeNthFromEnd(head, n)
    ListNode.print_list(res)


if __name__ == "__main__":
    main()