from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        M = len(board)
        N = len(board[0])

        os = set()
        edge_os = set()
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell == "O":
                    coord = i, j
                    if i in (0, M - 1) or j in (0, N - 1):
                        edge_os.add(coord)
                    else:
                        os.add(coord)

        queue = list(edge_os)
        while queue:
            coord = queue.pop()
            os.discard(coord)
            i, j = coord
            for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                coord = i + dx, j + dy
                x, y = coord
                if coord in edge_os or x < 0 or x >= M or y < 0 or y >= N or board[x][y] != "O":
                    continue
                edge_os.add(coord)
                queue.append(coord)

        for i, j in os:
            board[i][j] = "X"
