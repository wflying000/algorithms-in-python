"""
https://leetcode.cn/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/description/?envType=study-plan-v2&envId=coding-interviews
"""

from typing import List


class Solution:
    def trainingPlan(self, actions: List[int]) -> List[int]:
        i, j = 0, len(actions) - 1
        while i < j:
            while i < j and actions[i] % 2 != 0:
                i += 1
            while i < j and actions[j] % 2 == 0:
                j -= 1
            
            actions[i], actions[j] = actions[j], actions[i]
        
        return actions


def main():
    nums = [1, 2, 3, 4, 5]
    sln = Solution()
    sln.trainingPlan(nums)
    print(nums)


if __name__ == "__main__":
    main()