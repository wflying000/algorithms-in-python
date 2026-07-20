"""
https://leetcode.cn/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/description/?envType=study-plan-v2&envId=coding-interviews

"""

from data_structure.linked_list import ListNode 


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        p1, p2 = headA, headB
        while p1 != p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA

        return p1


def main():
    nums1 = [1, 2, 3]
    nums2 = [4, 5]
    nums3 = [6, 7, 8]
    l1 = ListNode.from_list(nums1)
    l2 = ListNode.from_list(nums2)
    l3 = ListNode.from_list(nums3)

    p1 = l1
    while p1.next is not None:
        p1 = p1.next
    p1.next = l3

    p2 = l2
    while p2.next is not None:
        p2 = p2.next
    p2.next = l3

    sln = Solution()
    intersec_node = sln.getIntersectionNode(l1, l2)
    print(intersec_node.val)


if __name__ == "__main__":
    main()