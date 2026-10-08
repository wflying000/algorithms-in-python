"""
https://leetcode.cn/problems/top-k-frequent-elements
"""

import heapq


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        heap = []
        for num, cnt in counts.items():
            if len(heap) < k:
                heapq.heappush(heap, (cnt, num))
            elif len(heap) == k:
                if heap[0][0] < cnt:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (cnt, num))
        
        res = [x[1] for x in heap]
        return res

def main():
    sln = Solution()
    nums = [1, 2, 1, 2, 1, 2, 3, 1, 3, 2]
    k = 2
    res = sln.topKFrequent(nums, k)
    print(res)


if __name__ == "__main__":
    main()