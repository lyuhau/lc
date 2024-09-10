from math import ceil
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i = 1
        j = max(piles) + 1
        while i != j:
            k = (i + j) // 2
            hours = sum(ceil(bs / k) for bs in piles)
            if hours <= h:
                j = k
            else:
                i = k + 1
        return i


if __name__ == '__main__':
    solution = Solution()
    # print(solution.minEatingSpeed([3, 6, 7, 11], 8))
    # print(solution.minEatingSpeed(piles = [1,4,3,2], h = 9))
    # print(solution.minEatingSpeed(piles = [25,10,23,4], h = 4))
