"""
https://leetcode.cn/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/description/?envType=study-plan-v2&envId=coding-interviews
"""

class Solution:
    def iceBreakingGame(self, num: int, target: int) -> int:
        res = 0
        for i in range(2, num + 1):
            res = (res + target) % i 
        
        return res


def main():
    sln = Solution()
    num = 10
    target = 3
    res = sln.iceBreakingGame(num, target)
    print(res)
    

if __name__ == "__main__":
    main()

