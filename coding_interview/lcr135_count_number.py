"""
https://leetcode.cn/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof/description/?envType=study-plan-v2&envId=coding-interviews
"""

from typing import List


class Solution:
    def countNumbers(self, cnt: int) -> List[int]:

        res = []
        # 先处理1位数，再处理2位数...
        for k in range(1, cnt + 1):
            self.dfs(k, [], res)
        return res

    # 处理num_digits位数
    def dfs(self, num_digits, buffer, res):
        if len(buffer) == num_digits:
            res.append(int("".join(buffer)))
            return

        for i in range(10):
            if len(buffer) == 0 and i == 0:
                continue
            buffer.append(str(i))
            self.dfs(num_digits, buffer, res)
            buffer.pop()


def main():
    sln = Solution()
    cnt = 2
    res = sln.countNumbers(cnt)
    print(res)


if __name__ == "__main__":
    main()