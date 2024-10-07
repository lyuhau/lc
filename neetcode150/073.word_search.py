from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, k):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[k]:
                return False
            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                board[i][j], tmp = '#', board[i][j]
                if k == len(word) - 1 or dfs(i + x, j + y, k + 1):
                    return True
                board[i][j] = tmp

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.exist([
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ], "ABCCED"))
    # print(s.exist([
    #     ["A"],
    # ], "A"))
