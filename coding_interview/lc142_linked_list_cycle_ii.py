"""
https://leetcode.cn/problems/linked-list-cycle-ii
"""

from typing import Optional

from data_structure.linked_list import ListNode


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                fast = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None


def main():
    sln = Solution()

    nums = [1, 2, 3, 4]
    head, nodes = ListNode.from_list(nums, with_nodes=True)
    nodes[-1].next = nodes[1]
    res = sln.detectCycle(head)
    print(res.val)

    nums = [1, 2, 3]
    head = ListNode.from_list(nums)
    res = sln.detectCycle(head)
    print(res)


if __name__ == "__main__":
    main()
