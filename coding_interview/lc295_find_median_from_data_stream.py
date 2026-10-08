"""
https://leetcode.cn/problems/find-median-from-data-stream/
"""

import heapq
import random

class MedianFinder:

    def __init__(self):
        self.min_heap = [] # 小顶堆，存放较大的数
        self.max_heap = [] # 大顶堆，存放较小的数

    def addNum(self, num: int) -> None:
        if len(self.min_heap) == len(self.max_heap):
            heapq.heappush(self.min_heap, num)
            x = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -x)
        else:
            heapq.heappush(self.max_heap, -num)
            x = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, x)


    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return 0.5 * (self.min_heap[0] - self.max_heap[0])
        return -self.max_heap[0]


def main():
    mf = MedianFinder()
    nums = [random.randint(0, 10) for _ in range(10)]
    print(nums)
    for idx, num in enumerate(nums):
        mf.addNum(num)
        median = mf.findMedian()
        nums2 = sorted(nums[:idx+1])
        if idx % 2 == 0:
            true_median = nums2[idx // 2]
        else:
            mid = idx // 2
            true_median = (nums2[mid] + nums2[mid + 1]) / 2

        assert median == true_median

        print(median)


if __name__ == "__main__":
    main()