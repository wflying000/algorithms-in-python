"""
https://leetcode.cn/problems/sort-list
"""

from typing import Optional

from data_structure.linked_list import ListNode


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        return self.mergeSort(head)
    
    def mergeSort(self, head):
        if not head or not head.next:
            return head
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        new_head = slow.next
        slow.next = None
        h1 = self.mergeSort(head)
        h2 = self.mergeSort(new_head)
        res = self.merge(h1, h2)
        return res
    
    def merge(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        dummy = ListNode()
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1 
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        
        if l1 is None:
            cur.next = l2
        else:
            cur.next = l1
        
        return dummy.next

def main():
    sln = Solution()
    nums = [5, 3, 2, 4, 1]
    head = ListNode.from_list(nums)
    res = sln.sortList(head)
    ListNode.print_list(res)


if __name__ == "__main__":
    main()
    