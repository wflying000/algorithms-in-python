"""
https://leetcode.cn/problems/spiral-matrix/

https://leetcode.cn/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/description/?envType=study-plan-v2&envId=coding-interviews

"""

from typing import List


class Solution:
    def spiralArray(self, array: List[List[int]]) -> List[int]:
        if not array:
            return []
        m, n = len(array), len(array[0])
        i, j = 0, 0
        s, t = m - 1, n - 1
        res = []
        while i <= s and j <= t:
            if i == s:
                for k in range(j, t + 1):
                    res.append(array[i][k])
                return res
            elif j == t:
                for k in range(i, s + 1):
                    res.append(array[k][j])
                return res
            
            for k in range(j, t):
                res.append(array[i][k])
            
            for k in range(i, s):
                res.append(array[k][t])
            
            for k in range(t, j, -1):
                res.append(array[s][k])
            
            for k in range(s, i, -1):
                res.append(array[k][j])
            
            i += 1
            j += 1
            s -= 1
            t -= 1
        
        return res


def main():
    array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    sln = Solution()
    res = sln.spiralArray(array)
    print(res)


if __name__ == "__main__":
    main()