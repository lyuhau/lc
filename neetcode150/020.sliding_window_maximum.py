import heapq
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums[:k]:
            counts.setdefault(num, [-num, 0])
            counts[num][1] += 1
        heap = list(counts.values())
        heapq.heapify(heap)

        result = [-heap[0][0]]

        for i, num in list(enumerate(nums))[k:]:
            if num not in counts:
                counts[num] = [-num, 0]
                heapq.heappush(heap, counts[num])
            counts[num][1] += 1
            counts[nums[i-k]][1] -= 1
            if counts[nums[i-k]][1] == 0:
                del(counts[nums[i-k]])
            while heap[0][1] == 0:
                heapq.heappop(heap)
            result.append(-heap[0][0])

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
    print(solution.maxSlidingWindow([1,2,1,0,4,2,6], 3))
