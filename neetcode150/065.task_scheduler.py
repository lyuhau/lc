from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = [0] * 26
        for task in tasks:
            counts[ord(task) - ord('A')] += 1
        counts.sort()
        max_count = counts.pop()
        num_max = counts.count(max_count) + 1
        return max(len(tasks), (max_count - 1) * (n + 1) + num_max)
