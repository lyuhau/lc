from typing import List


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def helper(start, target, current):
            if target == 0:
                result.append(current)
                return
            for i in range(start, len(nums)):
                if nums[i] > target:
                    continue
                helper(i, target - nums[i], current + [nums[i]])

        result = []
        helper(0, target, [])
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum([2, 3, 6, 7], 7))
