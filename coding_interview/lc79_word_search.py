"""
https://leetcode.cn/problems/word-search
"""


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if self.backtrack(board, word, i, j, 0):
                    return True
        return False


    def backtrack(self, board, word, x, y, idx):
        m, n = len(board), len(board[0])
        if x < 0 or x >= m or y < 0 or y >= n or board[x][y] != word[idx]:
            return False
        
        if idx == len(word) - 1:
            return True
            
        board[x][y] = ""
        res = self.backtrack(board, word, x - 1, y, idx + 1) or \
            self.backtrack(board, word, x + 1, y, idx + 1) or \
            self.backtrack(board, word, x, y - 1, idx + 1) or \
            self.backtrack(board, word, x, y + 1, idx + 1)
        
        board[x][y] = word[idx]
        return res


def main():
    sln = Solution()
    board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
    word = "ABCCED"
    res = sln.exist(board, word)
    print(res)


if __name__ == "__main__":
    main()