"""
https://leetcode.cn/problems/palindrome-linked-list
"""

from typing import Optional

from data_structure.linked_list import ListNode


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        return self.solution_1(head)
    
    def solution_1(self, head):
        if head is None:
            return False
        if head.next is None:
            return True
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        slow_next = slow.next
        slow.next = None

        head2 = self.reverse(slow_next)

        p1, p2 = head, head2
        res = True
        while p1 and p2:
            if p1.val != p2.val:
                res = False
                break
            p1 = p1.next
            p2 = p2.next
        slow.next = self.reverse(head2)

        return res


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

    nums1 = [1, 2, 2, 1]
    head1 = ListNode.from_list(nums1)
    res1 = sln.isPalindrome(head1)
    print(res1)

    nums2 = [1, 2, 3]
    head2 = ListNode.from_list(nums2)
    res2 = sln.isPalindrome(head2)
    print(res2)


if __name__ == "__main__":
    main()