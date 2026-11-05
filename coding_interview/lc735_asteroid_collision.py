"""
https://leetcode.cn/problems/asteroid-collision
"""


class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        res = []
        for x in asteroids:
            if x > 0:
                res.append(x)
                continue
            flag = True
            while res and res[-1] > 0:
                top = res[-1]
                if top <= -x:
                    res.pop()
                if top >= -x:
                    flag = False
                    break
            if flag:
                res.append(x)
        return res


def main():
    sln = Solution()
    asteroids = [5, 10, -5]
    res = sln.asteroidCollision(asteroids)
    print(res)


if __name__ == "__main__":
    main()