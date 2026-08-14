"""
https://leetcode.cn/problems/shu-zi-xu-lie-zhong-mou-yi-wei-de-shu-zi-lcof/description/?envType=study-plan-v2&envId=coding-interviews

https://leetcode.cn/problems/nth-digit/
"""


class Solution:
    def findKthNumber(self, k: int) -> int:
        if k < 10:
            return k
        num_bit = 1
        low, high = 1, 9
        start_index, end_index = 1, 9
        # 查找第k个数字所在的数是几位数
        while k > end_index:
            num_bit += 1
            low = high + 1
            high = 10**num_bit - 1
            num_numbers = 9 * (10 ** (num_bit - 1))
            start_index = end_index + 1
            end_index = end_index + num_numbers * num_bit

        offset = (k - start_index) // num_bit # num_bit位数的第几个数，从0计数
        number = low + offset # 第k个数位于哪个数字
        
        number_end_index = start_index + offset * num_bit + num_bit - 1 # number的最后一位的索引
        index_offset = number_end_index - k 
        for _ in range(index_offset):
            number = number // 10
        
        return number % 10



def main():
    sln = Solution()
    k = 190
    res = sln.findKthNumber(k)
    print(res)



if __name__ == "__main__":
    main()