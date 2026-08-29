"""
https://leetcode.cn/problems/reverse-nodes-in-k-group
"""

from typing import Optional

from data_structure.linked_list import ListNode


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head
        dummy = ListNode()
        pre = dummy
        cur = head
        while cur:
            first = cur
            i = 0
            while i < k - 1 and cur:
                i += 1
                cur = cur.next
            if not cur:
                pre.next = first
                break
            next = cur.next 
            cur.next = None
            pre.next = self.reverse(first)
            cur = next
            pre = first

        return dummy.next

    def reverse(self, head):
        pre = None
        while head:
            next = head.next
            head.next = pre
            pre = head
            head = next
        return pre


def main():
    sln = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    head = ListNode.from_list(nums)
    k = 3
    res = sln.reverseKGroup(head, k)
    ListNode.print_list(res)


if __name__ == "__main__":
    main()