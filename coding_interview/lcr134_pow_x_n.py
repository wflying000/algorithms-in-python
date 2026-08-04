"""
https://leetcode.cn/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/description/?envType=study-plan-v2&envId=coding-interviews

https://leetcode.cn/problems/powx-n/
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 1.0 or n == 0:
            return 1.0
        if x == 0.0:
            return 0.0
        
        is_pos = True if n > 0 else False
        N = n if n > 0 else -n
        
        res = self.pow(x, N)

        return res if is_pos else 1.0 / res

    
    def pow(self, x, n):
        if n == 1:
            return x
        if n == 0:
            return 1.0
        
        res = self.pow(x, n // 2)

        if n % 2 == 0:
            return res * res
        else:
            return res * res * x

def main():
    sln = Solution()
    print(sln.myPow(2.0, 3))
    print(sln.myPow(-3.0, 2))
    print(sln.myPow(2.0, -3))
    print(sln.myPow(-3.0, -2))

if __name__ == "__main__":
    main()
    