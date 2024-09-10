from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums)
        while i != j:
            check = (i + j) // 2
            if nums[check] == target:
                return check
            elif nums[check] > target:
                j = check
            else:
                i = check + 1
        return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.search([-1, 0, 3, 5, 9, 12], 9))
    # print(solution.search(nums = [-1,0,2,4,6,8], target = 4))
    # print(solution.search(nums = [-1,0,2,4,6,8], target = 3))
