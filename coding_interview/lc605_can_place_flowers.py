"""
https://leetcode.cn/problems/can-place-flowers
"""

class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        i, m = 0, len(flowerbed)
        while i < m:
            if n <= 0:
                break
            if (i == 0 or flowerbed[i - 1] == 0) and flowerbed[i] == 0 and (i == m - 1 or flowerbed[i + 1] == 0):
                n -= 1
                i += 2
            else:
                i += 1
        return n <= 0


def main():
    sln = Solution()
    flowerbed = [1, 0, 0, 0, 1]
    n = 1
    res = sln.canPlaceFlowers(flowerbed, n)
    print(res)


if __name__ == "__main__":
    main()