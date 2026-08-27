"""
https://leetcode.cn/problems/merge-two-sorted-lists
"""

from typing import Optional

from data_structure.linked_list import ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        
        dummy = ListNode(0)
        cur = dummy
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        
        if list1:
            cur.next = list1
        else:
            cur.next = list2
        
        return dummy.next

def main():
    sln = Solution()

    nums1 = [1, 2, 4]
    list1 = ListNode.from_list(nums1)

    nums2 = [1, 3, 4]
    list2 = ListNode.from_list(nums2)

    res = sln.mergeTwoLists(list1, list2)

    ListNode.print_list(res)


if __name__ == "__main__":
    main()