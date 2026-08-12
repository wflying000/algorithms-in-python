"""
https://leetcode.cn/problems/gou-jian-cheng-ji-shu-zu-lcof/?envType=study-plan-v2&envId=coding-interviews

https://leetcode.cn/problems/product-of-array-except-self/description/
"""

from typing import List


class Solution:
    def statisticalResult(self, arrayA: List[int]) -> List[int]:
        if not arrayA:
            return []
        res = [1 for _ in range(len(arrayA))]
        for i in range(1, len(arrayA)):
            res[i] = res[i - 1] * arrayA[i - 1] # res[i]记录arrayA[i]左侧元素的乘积
        
        right = 1
        for i in range(len(arrayA) - 1, -1, -1):
            res[i] = res[i] * right
            right = right * arrayA[i] # right记录arrayA[i]右侧元素的乘积
        
        return res


def main():
    sln = Solution()
    nums = [2, 4, 6, 8, 10]
    res = sln.statisticalResult(nums)
    print(res)


if __name__ == "__main__":
    main()