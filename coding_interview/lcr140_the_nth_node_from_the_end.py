"""
https://leetcode.cn/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/description/?envType=study-plan-v2&envId=coding-interviews

给定一个头节点为 head 的链表用于记录一系列核心肌群训练项目编号，请查找并返回倒数第 cnt 个训练项目编号对应的节点。

 
示例 1:

输入: head = [2,4,7,8], cnt = 1
输出: 8
 

提示：

1 <= head.length <= 100
0 <= head[i] <= 100
1 <= cnt <= head.length
 
"""

from typing import Optional
from data_structure.linked_list import ListNode


class Solution:
    def trainingPlan(self, head: Optional[ListNode], cnt: int) -> Optional[ListNode]:
        if head is None:
            return None
        
        p1 = head
        for _ in range(cnt):
            p1 = p1.next
        p2 = head
        while p1 is not None:
            p1 = p1.next
            p2 = p2.next
        return p2


def main():
    nums = [1, 2, 3, 4]
    head = ListNode.from_list(nums)
    sln = Solution()
    for cnt in range(1, len(nums) + 1):
        node = sln.trainingPlan(head, cnt)
        assert node.val == nums[-cnt]


if __name__ == "__main__":
    main()