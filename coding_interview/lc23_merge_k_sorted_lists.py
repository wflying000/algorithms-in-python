"""
https://leetcode.cn/problems/merge-k-sorted-lists
"""

from typing import Optional, List

from data_structure.linked_list import ListNode


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        return self.merge_lists(lists, 0, len(lists) - 1)

    def merge_lists(self, lists, left, right):
        if left > right:
            return None
        elif left == right:
            return lists[left]
        
        mid = (right - left) // 2 + left
        l1 = self.merge_lists(lists, left, mid)
        l2 = self.merge_lists(lists, mid + 1, right)

        res = self.merge(l1, l2)

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
    nums_list = [[1, 6, 7], [3, 6, 8], [2, 4, 5]]
    lists = [ListNode.from_list(x) for x in nums_list]
    res = sln.mergeKLists(lists)
    ListNode.print_list(res)


if __name__ == "__main__":
    main()