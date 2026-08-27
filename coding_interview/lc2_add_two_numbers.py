"""
https://leetcode.cn/problems/add-two-numbers
"""

from typing import Optional

from data_structure.linked_list import ListNode


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not l1:
            return l2
        elif not l2:
            return l1

        c = 0
        res = None
        while l1 or l2:
            if l1:
                a = l1.val 
                l1 = l1.next
            else:
                a = 0
            if l2:
                b = l2.val
                l2 = l2.next
            else:
                b = 0
            s = a + b + c
            c = s // 10
            s = s % 10
            node = ListNode(s)
            if res is not None:
                 pre.next = node
                 pre = pre.next
            else:
                res = node
                pre = node 
        if c != 0:
            pre.next = ListNode(c)
        return res


def main():
    sln = Solution()

    nums1 = [1, 2, 3]
    l1 = ListNode.from_list(nums1)

    nums2 = [3, 8, 9]
    l2 = ListNode.from_list(nums2)

    res = sln.addTwoNumbers(l1, l2)
    ListNode.print_list(res)


if __name__ == "__main__":
    main()
