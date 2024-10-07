import heapq

from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)[-k:]
        heapq.heapify(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]


if __name__ == '__main__':
    s = KthLargest(3, [1, 2, 3, 3])
    print(s.add(3))
    print(s.add(5))
    print(s.add(6))
    print(s.add(7))
    print(s.add(8))
