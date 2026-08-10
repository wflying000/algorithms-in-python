"""
https://leetcode.cn/problems/chou-shu-lcof/description/?envType=study-plan-v2&envId=coding-interviews

https://leetcode.cn/problems/ugly-number-ii/
"""


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = [1]
        p2, p3, p5 = 0, 0, 0
        for i in range(n - 1):
            num2 = nums[p2] * 2
            num3 = nums[p3] * 3
            num5 = nums[p5] * 5

            num = min(num2, min(num3, num5))

            if num == num2:
                p2 += 1
            if num == num3:
                p3 += 1
            if num == num5:
                p5 += 1
            
            nums.append(num)
        
        return nums[n - 1]
        

def main():
    ugly_numbers = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12]
    sln = Solution()
    for idx, num in enumerate(ugly_numbers):
        res = sln.nthUglyNumber(idx + 1)
        assert res == num


if __name__ == "__main__":
    main()