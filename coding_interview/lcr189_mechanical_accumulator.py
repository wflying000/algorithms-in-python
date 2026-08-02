"""
https://leetcode.cn/problems/qiu-12n-lcof/description/?envType=study-plan-v2&envId=coding-interviews

请设计一个机械累加器，计算从 1、2... 一直累加到目标数值 target 的总和。注意这是一个只能进行加法操作的程序，不具备乘除、if-else、switch-case、for 循环、while 循环，及条件判断语句等高级功能。
"""

class Solution:
    def mechanicalAccumulator(self, target: int) -> int:
        return target and (target + self.mechanicalAccumulator(target - 1))


def main():
    sln = Solution()
    target = 5
    s = (1 + target) * target // 2
    res = sln.mechanicalAccumulator(target)
    assert res == s
    print(res)


if __name__ == "__main__":
    main()
