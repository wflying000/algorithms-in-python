"""
https://leetcode.cn/problems/fan-zhuan-lian-biao-lcof/?envType=study-plan-v2&envId=coding-interviews

"""

from typing import Optional

from data_structure.linked_list import ListNode


class Solution:
    def trainningPlan(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.trainning_recursive(head)

    def trainning_recursive(self, head):
        if head == None or head.next == None:
            return head
        res = self.trainning_recursive(head.next)
        head.next.next = head
        head.next = None
        return res

    def trainning_iterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        while head:
            next = head.next
            head.next = pre 
            pre = head
            head = next
        return pre
    

def main():
    nums = [1, 2, 3]
    head = ListNode.from_list(nums)
    ListNode.print_list(head)
    sln = Solution()
    new_head = sln.trainningPlan(head)
    ListNode.print_list(new_head)
    

if __name__ == "__main__":
    main()
