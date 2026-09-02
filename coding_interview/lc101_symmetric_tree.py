"""
https://leetcode.cn/problems/symmetric-tree
"""

from typing import Optional
from collections import deque

from data_structure.binary_tree import TreeNode



class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        # return self.judge_symmetric_recur(root.left, root.right)

        return self.judge_symmetric_iter(root, root)
    
    def judge_symmetric_recur(self, t1, t2):
        if not t1 and not t2:
            return True

        if not t1 or not t2:
            return False

        if t1.val != t2.val:
            return False
        
        return self.judge_symmetric_recur(t1.left, t2.right) and self.judge_symmetric_recur(t1.right, t2.left)
                
    
    def judge_symmetric_iter(self, t1, t2):
        queue = deque()
        queue.append(t1)
        queue.append(t2)

        while queue:
            t1 = queue.popleft()
            t2 = queue.popleft()

            if not t1 and not t2:
                continue
            elif (not t1 or not t2) or (t1.val != t2.val):
                return False
            
            queue.append(t1.left)
            queue.append(t2.right)

            queue.append(t1.right)
            queue.append(t2.left)
        
        return True
            

def main():
    sln = Solution()
    nums1 = [1, 2, 2, 3, 4, 4, 3]
    root1 = TreeNode.from_list(nums1)
    res1 = sln.isSymmetric(root1)
    print(res1)

    nums2 = [1, 2, 2, None, 3, None, 3]
    root2 = TreeNode.from_list(nums2)
    res2 = sln.isSymmetric(root2)
    print(res2)


if __name__ == "__main__":
    main()