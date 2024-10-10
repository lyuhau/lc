from typing import List


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        M = len(grid)
        N = len(grid[0])

        treasures = [
            (i, j)
            for i, row in enumerate(grid)
            for j, cell in enumerate(row)
            if cell == 0
        ]

        queue = treasures
        while queue:
            i, j = queue.pop(0)
            val = grid[i][j]
            for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                x, y = i + dx, j + dy
                if x < 0 or x >= M or y < 0 or y >= N:
                    continue
                if grid[x][y] > val + 1:
                    grid[x][y] = val + 1
                    queue.append((x, y))
