"""
https://leetcode.cn/problems/copy-list-with-random-pointer
"""

from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        cur = head
        while cur:
            cur.next = Node(cur.val, next=cur.next)
            cur = cur.next.next
        
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        
        res = head.next
        pre = head
        cur = head.next
        while cur.next:
            pre.next = pre.next.next
            cur.next = cur.next.next
            pre = pre.next
            cur = cur.next

        return res
