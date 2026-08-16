"""
https://leetcode.cn/problems/number-of-digit-one/

给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。
"""

class Solution:
    def countDigitOne(self, num: int) -> int:
        if num == 0:
            return 0
        if num <= 9:
            return 1

        # 第一步：累加 1 ~ 最大的 (b-1) 位数 中 '1' 的总个数
        # d 位数（10^(d-1)..10^d-1）中 '1' 的个数：
        #   最高位为 1 的有 10^(d-1) 个；
        #   其余 d-1 个数位各贡献 9 * 10^(d-2) 次。
        res = 1                  # 1..9 中 '1' 的个数
        high = 99
        num_bits = 2
        while high < num:
            res += 10 ** (num_bits - 1) + 9 * (10 ** (num_bits - 2)) * (num_bits - 1)
            num_bits += 1
            high = 10 ** num_bits - 1

        # 此时 num_bits == b（num 的位数），res = 1..10^(b-1)-1 中 '1' 的总个数
        L = 10 ** (num_bits - 1)     # 最小的 b 位数

        # 第二步：累加 [L, num] 中 '1' 的个数
        # 最高位：为 '1' 的 b 位数即 [L, min(num, 2L-1)]
        res += max(0, min(num, 2 * L - 1) - L + 1)

        # 其余 b-1 个数位逐位统计 [L, num] 内该位为 '1' 的个数
        # 对数位权重 w，先按经典公式统计 [0, num] 中该位为 '1' 的次数，
        # 再减去 [0, L-1] 中该位为 '1' 的次数（恰好是 10^(b-2)，且已计入 res）
        w = 1
        while w < L:
            high_part = num // (10 * w)
            cur = (num // w) % 10
            low_part = num % w
            if cur == 0:
                cnt = high_part * w
            elif cur == 1:
                cnt = high_part * w + low_part + 1
            else:
                cnt = (high_part + 1) * w
            res += cnt - 10 ** (num_bits - 2)
            w *= 10

        return res


def count_ones_brute_force(num):
    return sum(str(x).count("1") for x in range(num + 1))


def main():
    sln = Solution()
    nums = [0, 1, 9, 10, 11, 13, 99, 100, 523, 1000, 3141592]
    for num in nums:
        res = sln.countDigitOne(num)
        expected = count_ones_brute_force(num) if num <= 100000 else None
        print(f"num={num:>8}  countDigitOne={res}")
        assert expected is None or res == expected


if __name__ == "__main__":
    main()
