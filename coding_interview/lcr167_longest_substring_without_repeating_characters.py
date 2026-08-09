"""
https://leetcode.cn/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof/description/?envType=study-plan-v2&envId=coding-interviews\

https://leetcode.cn/problems/longest-substring-without-repeating-characters/

"""


class Solution:
    def dismantlingAction(self, arr: str) -> int:
        if not arr:
            return 0
        ch2idx = {}
        res = 0
        start = 0 # 当前最长无重复子串的起始位置
        for idx, ch in enumerate(arr):
            start = max(start, ch2idx.get(ch, -1) + 1) # 更新起始位置
            res = max(res, idx - start + 1) 
            ch2idx[ch] = idx
        return res


def main():
    arr = "pwwkew"
    sln = Solution()
    res = sln.dismantlingAction(arr)
    print(res)


if __name__ == "__main__":
    main()


