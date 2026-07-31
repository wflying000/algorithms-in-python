"""
https://leetcode.cn/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/?envType=study-plan-v2&envId=coding-interviews
"""


class Solution:
    def wardrobeFinishing(self, m: int, n: int, cnt: int) -> int:
        visited = [[False for _ in range(n)] for _ in range(m)]

        return self.process(m, n, cnt, visited, 0, 0)

    def process(self, m, n, cnt, visited, i, j):
        if (i < 0) or (i >= m) or (j < 0) or (j >= n) or (self.digit(i) + self.digit(j) > cnt) or visited[i][j]:
            return 0
        visited[i][j] = True
        return 1 + self.process(m, n, cnt, visited, i, j + 1) + self.process(m, n, cnt, visited, i + 1, j)
    
    def digit(self, x):
        s = 0
        while x > 0:
            s += x % 10
            x = x // 10
        return s


def main():
    m, n, cnt = 4, 7, 5
    sln = Solution()
    res = sln.wardrobeFinishing(m, n, cnt)
    print(res)


if __name__ == "__main__":
    main()