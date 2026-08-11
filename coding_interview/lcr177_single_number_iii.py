"""
https://leetcode.cn/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/description/?envType=study-plan-v2&envId=coding-interviews

https://leetcode.cn/problems/single-number-iii/
"""

from typing import List


class Solution:
    def sockCollocation(self, nums: List[int]) -> List[int]:
        # 数组中恰好有两个元素只出现一次，其余所有元素均出现两次
        # 假设只出现一次的两个元素分别为a, b

        # 对整个数组进行异或操作，由于其余元素都出现两次，因此最后异或结果是a、b的异或，即xor == a ^ b
        xor = 0
        for s in nums:
            xor = xor ^ s 

        # 由于a != b, 那么a和b的二进制表示中至少有一位不同，找出一个不同位
        num = 1
        while num & xor == 0:
            num = num << 1

        # 通过与num进行&操作将数组中的所有数分组，那么a, b必然被分到两个不同的组
        # 两个组内的元素进行异或之后，即可得到a、b两个数
        a, b = 0, 0
        for s in nums:
            if s & num == 0:
                a = a ^ s
            else:
                b = b ^ s
        
        return [a, b]
        

def main():
    nums = [1, 1, 2, 3, 4, 4, 5, 5]
    sln = Solution()
    res = sln.sockCollocation(nums)
    print(res)


if __name__ == "__main__":
    main()