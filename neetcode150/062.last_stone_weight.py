from typing import List

import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            a = -heapq.heappop(stones)
            b = -heapq.heappop(stones)
            if a == b:
                continue
            else:
                heapq.heappush(stones, b - a)
        return -stones[0] if stones else 0
