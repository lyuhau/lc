from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        M = len(heights)
        N = len(heights[0])

        def unflood(queue):
            watershed = set(queue)
            while queue:
                coord = queue.pop()
                i, j = coord
                height = heights[i][j]
                for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                    coord = i + dx, j + dy
                    x, y = coord
                    if coord in watershed or x < 0 or x >= M or y < 0 or y >= N:
                        continue
                    if heights[x][y] >= height:
                        watershed.add(coord)
                        queue.append(coord)
            return watershed

        pacific_watershed = unflood([
            *((i, 0) for i in range(M)),
            *((0, j) for j in range(1, N)),
        ])
        atlantic_watershed = unflood([
            *((i, N - 1) for i in range(M)),
            *((M - 1, j) for j in range(N)),
        ])

        return list(pacific_watershed.intersection(atlantic_watershed))
