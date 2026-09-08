"""
https://leetcode.cn/problems/path-sum-iii
"""

from typing import Optional

from data_structure.binary_tree import TreeNode


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # self.res = 0
        # self.path_sum(root, targetSum)
        # return self.res

        sum2count = {0: 1}
        return self.dfs(root, targetSum, 0, sum2count)

    
    def dfs(self, root, target_sum, pre_sum, sum2count):
        if  not root:
            return 0
        res = 0
        pre_sum += root.val
        res += sum2count.get(pre_sum - target_sum, 0)
        sum2count[pre_sum] = sum2count.get(pre_sum, 0) + 1
        res += self.dfs(root.left, target_sum, pre_sum, sum2count)
        res += self.dfs(root.right, target_sum, pre_sum, sum2count)
        sum2count[pre_sum] -= 1

        return res
    
    def path_sum(self, root, targetSum):
        if not root:
            return []
        
        
        left = self.path_sum(root.left, targetSum)
        right = self.path_sum(root.right, targetSum)

        left_sum = [x + root.val for x in left]
        right_sum = [x + root.val for x in right]
        result = left_sum + right_sum + [root.val]

        self.res += sum([1 for x in result if x == targetSum])

        return result



def main():
    sln = Solution()
    nums = [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]
    root = TreeNode.from_list(nums)
    target_sum = 8
    res = sln.pathSum(root, target_sum)
    print(res)


if __name__ == "__main__":
    main()
