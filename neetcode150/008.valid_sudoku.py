from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        groups_funcs = [
            lambda i, j: board[i][j],
            lambda i, j: board[j][i],
            lambda i, j: board[i // 3 * 3 + j // 3][i % 3 * 3 + j % 3],
        ]
        for i in range(9):
            for group_func in groups_funcs:
                group = [x for j in range(9) if (x := group_func(i, j)) != '.']
                print(group)
                if len(group) != len(set(group)):
                    return False
        return True
