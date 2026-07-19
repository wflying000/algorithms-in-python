"""
https://leetcode.cn/problems/fu-za-lian-biao-de-fu-zhi-lcof/?envType=study-plan-v2&envId=coding-interviews
"""

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        return self.copyRandomList_1(head)

    def copyRandomList_map(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        maps = {}
        cur = head
        while cur:
            maps[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            new_cur = maps[cur]
            new_cur.next = maps.get(cur.next)
            new_cur.random = maps.get(cur.random)
            cur = cur.next
        
        return maps[head]
        

    def copyRandomList_o1(self, head: 'Node') -> 'Node':
        cur = head
        if head is None:
            return None
        
        while cur:
            ori_next = cur.next
            cur.next = Node(cur.val, ori_next)
            cur = ori_next

        cur = head
        while cur:
            if cur.random is not None:
                cur.next.random = cur.random.next
            cur = cur.next.next
        
        res = head.next
        # cur = head
        # while cur:
        #     new_cur = cur.next
        #     cur.next = new_cur.next
        #     if cur.next is not None:
        #         new_cur.next = cur.next.next
        #     else:
        #         break

        cur = head.next
        pre = head
        while cur.next:
            pre.next = pre.next.next
            cur.next = cur.next.next
            pre = pre.next
            cur = cur.next
        pre.next = None
        
        return res


