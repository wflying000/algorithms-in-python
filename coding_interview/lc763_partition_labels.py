"""
https://leetcode.cn/problems/partition-labels
"""

class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        ch2pos = {}
        for i, ch in enumerate(s):
            ch2pos[ch] = i 
        res = []
        start, end = 0, 0
        for i, ch in enumerate(s):
            end = max(end, ch2pos[ch])
            if i == end:
                res.append(end - start + 1)
                start = end + 1
        return res

    def partitionLabels1(self, s: str) -> list[int]:
        ch2pos = {}
        for idx, ch in enumerate(s):
            if ch not in ch2pos:
                ch2pos[ch] = [idx, idx]
            ch2pos[ch][1] = idx 
        indexes = [v for k, v in ch2pos.items()]
        indexes = sorted(indexes, key=lambda x: (x[0], x[1]))
        start_idx = indexes[0][0]
        end_idx = indexes[0][1]
        res = []
        for i, pair in enumerate(indexes):
            if pair[0] >  end_idx:
                res.append(end_idx - start_idx + 1)
                start_idx = pair[0]
                end_idx = pair[1]
            else:
                end_idx = max(end_idx, pair[1])
            if i == len(indexes) - 1:
                res.append(end_idx - start_idx + 1)

        return res


def main():
    sln = Solution()
    s = "eccbbbbdec"
    res = sln.partitionLabels(s)
    print(res)


if __name__ == "__main__":
    main()