from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        M = len(grid)
        N = len(grid[0])

        count = 0
        seen = set()
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                coord = i, j

                # already explored
                if coord in seen:
                    continue

                # water
                if cell == "0":
                    continue

                # land ho!
                count += 1

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
                    if grid[x][y] == "0":
                        continue
                    # more land, continue exploring
                    for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                        queue.append((x + dx, y + dy))

        return count
