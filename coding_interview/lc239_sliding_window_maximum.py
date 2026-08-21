"""
https://leetcode.cn/problems/sliding-window-maximum
"""

from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
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
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    label = [3, 3, 5, 5, 6, 7]
    res = sln.maxSlidingWindow(nums, k)
    print(res)
    assert res == label


if __name__ == "__main__":
    main()