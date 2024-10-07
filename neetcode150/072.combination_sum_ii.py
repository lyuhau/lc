from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(index, target, current):
            if target == 0:
                result.add(tuple(current))
                return
            if index == len(candidates) or target < candidates[index]:
                return
            helper(index + 1, target, current)
            helper(index + 1, target - candidates[index], current + [candidates[index]])

        result = set()
        candidates.sort()
        helper(0, target, [])
        return [list(t) for t in result]


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
