"""
https://leetcode.cn/problems/zui-xiao-de-kge-shu-lcof/?envType=study-plan-v2&envId=coding-interviews
"""

from typing import List

class Solution:
    def inventoryManagement(self, stock: List[int], cnt: int) -> List[int]:
        if cnt >= len(stock):
            return stock
        
        def quick_sort(nums, left, right):
            i, j = left, right
            pivot = nums[left]
            while i < j:
                while i < j and nums[j] >= pivot:
                    j -= 1
                while i < j and nums[i] <= pivot:
                    i += 1
                
                nums[i], nums[j] = nums[j], nums[i]
            
            nums[left], nums[i] = nums[i], nums[left]

            if cnt < i:
                return quick_sort(nums, left, i - 1)
            elif cnt > i:
                return quick_sort(nums, i + 1, right)
            
            return nums[:cnt]
        
        return quick_sort(stock, 0, len(stock) - 1)


def main():
    nums = [3, 2, 1, 5, 4]
    sln = Solution()
    cnt = 2 
    res = sln.inventoryManagement(nums, cnt)
    print(res)


if __name__ == "__main__":
    main()
