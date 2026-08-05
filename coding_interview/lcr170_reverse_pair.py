"""
https://leetcode.cn/problems/shu-zu-zhong-de-ni-xu-dui-lcof/?envType=study-plan-v2&envId=coding-interviews
"""

from typing import List


class Solution:
    def reversePairs(self, record: List[int]) -> int:
        
        return self.merge_sort(record, 0, len(record) - 1)
    
    def merge_sort(self, record, left, right):
        if left >= right:
            return 0
        mid = (right - left) // 2 + left
        
        count1 = self.merge_sort(record, left, mid)
        count2 = self.merge_sort(record, mid + 1, right)

        count3 = self.merge(record, left, mid, right)

        return count1 + count2 + count3
    
    def merge(self, record, left, mid, right):
        num = right - left + 1
        tmp = [0 for _ in range(num)]
        count = 0
        i, j, k = mid, right, num - 1
        while i >= left and j > mid:
            if record[i] <= record[j]:
                tmp[k] = record[j]
                j -= 1
                k -= 1
            else:
                tmp[k] = record[i]
                count += j - mid
                i -= 1
                k -= 1
        while i >= left:
            tmp[k] = record[i]
            i -= 1
            k -= 1
        while j > mid:
            tmp[k] = record[j]
            j -= 1
            k -= 1

        
        for k in range(num):
            record[left + k] = tmp[k]
        
        return count


def main():
    sln = Solution()
    nums = [9, 7, 5, 4, 6]
    res = sln.reversePairs(nums)
    print(res)
    print(nums)


if __name__ == "__main__":
    main()