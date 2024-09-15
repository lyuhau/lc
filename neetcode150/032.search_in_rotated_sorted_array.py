from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[0] < nums[-1]:
            return binary_search(nums, target)
        else:
            return rotated_binary_search(nums, target)


def binary_search(nums: List[int], target: int) -> int:
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


def rotated_binary_search(nums: List[int], target: int) -> int:
    i = 0
    j = len(nums)
    while i != j:
        check_i = (i + j) // 2
        check = nums[check_i]
        if check == target:
            return check_i
        elif check > nums[0]:
            if target < check:
                i = check_i
            else:
                j = check_i + 1
        else:
            if target < check:
                j = check_i
            else:
                i = check_i + 1
    return -1


if __name__ == '__main__':
    solution = Solution()
    # print(solution.search([-1, 0, 3, 5, 9, 12], 9))
    # print(solution.search(nums = [4,5,6,7,0,1,2], target = 0))
    print(solution.search(nums = [3,4,5,6,1,2], target = 1))
