"""
https://leetcode.cn/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/description/?envType=study-plan-v2&envId=coding-interviews
"""

from typing import List


class Solution:
    def verifyTreeOrder(self, postorder: List[int]) -> bool:
        if not postorder:
            return True

        n = len(postorder)

        return self.verify(postorder, 0, n - 1)
        
    
    def verify(self, postorder, left, right):
        if left >= right:
            return True

        i = left
        while i < right and postorder[i] < postorder[right]:
            i += 1
        j = i
        while j < right and postorder[j] > postorder[right]:
            j += 1
        return j == right and self.verify(postorder, left, i - 1) and self.verify(postorder, i, right - 1)


def main():
    postorder = [4, 9, 6, 5, 8]
    sln = Solution()
    res = sln.verifyTreeOrder(postorder)
    print(res)


if __name__ == "__main__":
    main()