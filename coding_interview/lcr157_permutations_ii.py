"""
https://leetcode.cn/problems/zi-fu-chuan-de-pai-lie-lcof/description/?envType=study-plan-v2&envId=coding-interviews

https://leetcode.cn/problems/permutations-ii/description/
"""

from typing import List

class Solution:
    def goodsOrder(self, goods: str) -> List[str]:
        if not goods:
            return [""]
        
        visited = [False for _ in range(len(goods))]
        goods = sorted(goods)
        res = []
        self.dfs(goods, [], visited, res)

        return res
    
    def dfs(self, goods, chs, visited, res):
        if len(chs) == len(goods):
            res.append("".join(chs))
            return
        
        for i in range(len(goods)):
            if visited[i] or (i > 0 and goods[i] == goods[i - 1] and not visited[i - 1]):
                continue
            chs.append(goods[i])
            visited[i] = True
            self.dfs(goods, chs, visited, res)
            chs.pop()
            visited[i] = False

def main():
    strs = "abbcd"
    sln = Solution()
    res = sln.goodsOrder(strs)
    print(res)


if __name__ == "__main__":
    main()