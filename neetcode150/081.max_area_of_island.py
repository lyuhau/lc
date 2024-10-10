from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])

        biggest_seen = 0
        seen = set()
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                coord = i, j

                # already explored
                if coord in seen:
                    continue

                # water
                if cell == 0:
                    continue

                # land ho! start measuring the island size
                size = 0

                # dfs to mark all attached land as seen
                queue = [coord]
                while queue:
                    coord = queue.pop()
                    if coord in seen:
                        continue
                    x, y = coord
                    if x < 0 or x >= M or y < 0 or y >= N:
                        continue
                    seen.add(coord)
                    if grid[x][y] == 0:
                        continue
                    size += 1
                    # more land, continue exploring
                    for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                        queue.append((x + dx, y + dy))
                biggest_seen = max(biggest_seen, size)

        return biggest_seen
