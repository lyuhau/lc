from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])

        rotten_bananas = [
            (i, j)
            for i, row in enumerate(grid)
            for j, cell in enumerate(row)
            if cell == 2
        ]

        for i, j in rotten_bananas:
            grid[i][j] = -1

        val = -1
        queue = rotten_bananas
        while queue:
            i, j = queue.pop(0)
            val = grid[i][j]
            for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                x, y = i + dx, j + dy
                if x < 0 or x >= M or y < 0 or y >= N:
                    continue
                if grid[x][y] == 1:
                    grid[x][y] = val - 1
                    queue.append((x, y))

        if any(cell == 1 for row in grid for cell in row):
            return -1

        return -val - 1
