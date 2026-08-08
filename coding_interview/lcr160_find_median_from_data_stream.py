"""
https://leetcode.cn/problems/shu-ju-liu-zhong-de-zhong-wei-shu-lcof/description/?envType=study-plan-v2&envId=coding-interviews

https://leetcode.cn/problems/find-median-from-data-stream/
"""

import heapq
import random

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:

        self.add_num_clean(num)

    def findMedian(self) -> float:

        return self.find_median_clean()
    
    
    def add_num_detail(self, num: int) -> None:
            
        if (not self.max_heap) and (not self.min_heap):
            heapq.heappush(self.min_heap, num)
        elif len(self.max_heap) > len(self.min_heap):
            heapq.heappush(self.max_heap, -num)
            x = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, x)
        elif len(self.max_heap) < len(self.min_heap):
            heapq.heappush(self.min_heap, num)
            x = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -x)
        elif len(self.max_heap) == len(self.min_heap):
            if num <= -self.max_heap[0]:
                heapq.heappush(self.max_heap, -num)
            else:
                heapq.heappush(self.min_heap, num)


    def find_median_detail(self) -> float:
            
        if (not self.min_heap) and (not self.max_heap):
            return None
        elif not self.min_heap:
            return -self.max_heap[0]
        elif not self.max_heap:
            return self.min_heap[0]
        elif len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        elif len(self.min_heap) < len(self.max_heap):
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0]) * 0.5

    def find_median_clean(self):
        if len(self.min_heap) != len(self.max_heap):
            return self.min_heap[0]
        
        return (-self.max_heap[0] + self.min_heap[0]) / 2
    
    def add_num_clean(self, num):
        if len(self.min_heap) != len(self.max_heap):
            heapq.heappush(self.min_heap, num)
            x = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -x)
        else:
            heapq.heappush(self.max_heap, -num)
            x = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, x)


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