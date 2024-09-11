from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]

        i = 0
        j = len(nums)
        while i != j:
            check = (i + j) // 2
            if nums[check] > nums[i]:
                i = check
            else:
                j = check
        return nums[i + 1]


if __name__ == '__main__':
    solution = Solution()
    # print(solution.findMin([3, 4, 5, 1, 2]))
    print(solution.findMin(nums = [3, 4, 5, 6, 1, 2]))
    print(solution.findMin(nums = [1, 2, 3, 4, 5, 6]))
    print(solution.findMin(nums = [4,5,6,7]))
