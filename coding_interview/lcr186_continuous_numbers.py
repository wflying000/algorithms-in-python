"""
https://leetcode.cn/problems/bu-ke-pai-zhong-de-shun-zi-lcof/?envType=study-plan-v2&envId=coding-interviews
"""

from typing import List

class Solution:
    def checkDynasty(self, places: List[int]) -> bool:
        min_v = float('inf')
        max_v = float('-inf')
        nums = set()
        for x in places:
            if x == 0:
                continue
            if x in nums:
                return False
            nums.add(x)
            min_v = min(x, min_v)
            max_v = max(x, max_v)
        
        return  max_v - min_v <= 4 
        

def main():
    sln = Solution()
    places = [0, 6, 9, 0, 7]
    res = sln.checkDynasty(places)
    print(res)


if __name__ == "__main__":
    main()