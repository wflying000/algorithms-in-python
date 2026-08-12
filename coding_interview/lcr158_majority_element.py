"""
https://leetcode.cn/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/description/?envType=study-plan-v2&envId=coding-interviews

https://leetcode.cn/problems/majority-element/
"""

from typing import List


class Solution:
    def inventoryManagement(self, stock: List[int]) -> int:
        # 投票法
        # 假设最多元素为x, 遍历元素，出现相同元素计数加一，出现不同元素计数减一，当计数为0时更换x的值，最后x的值就是超过一半的数
        res = None
        count = 0
        for s in stock:
            if count == 0:
                res = s 
            if res == s:
                count += 1
            else:
                count -= 1
        
        return res

def main():
    sln = Solution()
    nums = [6, 1, 3, 1, 1, 1]
    res = sln.inventoryManagement(nums)
    print(res)


if __name__ == "__main__":
    main()