"""
https://leetcode.cn/problems/swap-nodes-in-pairs/
"""

from typing import Optional

from data_structure.linked_list import ListNode


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        res = head.next
        node = head.next.next
        head.next.next = head
        pre = head
        pre.next = None
        while node:
            if not node.next:
                pre.next = node
                break
            node2 = node.next
            node.next = None
            next = node2.next
            node2.next = node 
            pre.next = node2
            pre = node 
            node = next
        return res        



def main():
    sln = Solution()
    nums = [1, 2, 3, 4]
    head = ListNode.from_list(nums)
    res = sln.swapPairs(head)

    ListNode.print_list(res)


if __name__ == "__main__":
    main()