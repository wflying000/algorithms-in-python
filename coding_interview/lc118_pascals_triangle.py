"""
https://leetcode.cn/problems/pascals-triangle
"""


class Solution:
    def generate(self, numRows: int) -> list[list[int]]:

        res = []
        for i in range(numRows):
            row = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(res[i - 1][j - 1] + res[i - 1][j])
            res.append(row)
        
        return res


def main():
    sln = Solution()
    n = 5
    res = sln.generate(n)
    print(res)


if __name__ == "__main__":
    main()