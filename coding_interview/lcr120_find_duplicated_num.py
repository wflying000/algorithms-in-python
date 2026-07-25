"""
https://leetcode.cn/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/solutions/96623/mian-shi-ti-03-shu-zu-zhong-zhong-fu-de-shu-zi-yua/?envType=study-plan-v2&envId=coding-interviews

给定一个长度度为n的数组，其中元素范围是 0 到 n-1，返回任意一个重复元素
"""

from typing import List


class Solution:
    def findRepeatDocument(self, documents: List[int]) -> int:
        
        for i in range(len(documents)):
            while documents[i] != i:
                j = documents[i]
                if documents[j] == j:
                    return j
                documents[i], documents[j] = documents[j], documents[i]
        
        return -1


def main():
    nums = [2, 5, 3, 0, 5, 0]
    sln = Solution()
    res = sln.findRepeatDocument(nums)
    print(res)


if __name__ == "__main__":
    main()