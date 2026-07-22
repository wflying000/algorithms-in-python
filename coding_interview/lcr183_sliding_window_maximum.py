"""
https://leetcode.cn/problems/sliding-window-maximum/description/

https://leetcode.cn/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/description/?envType=study-plan-v2&envId=coding-interviews
"""

from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        queue = deque()
        for i in range(k - 1):
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
            queue.append(i)
        
        res = []
        for i in range(k - 1, len(nums)):
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
            queue.append(i)
            if i - queue[0] >= k:
                queue.popleft()
            res.append(nums[queue[0]])
        
        return res


def main():
    sln = Solution()
    nums = [14, 2, 27, -5, 28, 13, 39]
    k = 3
    expected = [27, 27, 28, 28, 39]
    res = sln.maxSlidingWindow(nums, k)
    assert res == expected


if __name__ == "__main__":
    main()


