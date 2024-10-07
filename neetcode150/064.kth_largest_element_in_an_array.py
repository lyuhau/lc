from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(i, j):
            pivot_value = nums[j]
            pivot_pointer = i
            for n in range(i, j):
                if nums[n] < pivot_value:
                    nums[n], nums[pivot_pointer] = nums[pivot_pointer], nums[n]
                    pivot_pointer += 1
            nums[pivot_pointer], nums[j] = nums[j], nums[pivot_pointer]
            return pivot_pointer

        k = len(nums) - k
        i, j = 0, len(nums) - 1
        while i <= j:
            pivot_pointer = partition(i, j)
            if pivot_pointer == k:
                return nums[pivot_pointer]
            elif pivot_pointer < k:
                i = pivot_pointer + 1
            else:
                j = pivot_pointer - 1
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.findKthLargest([2, 3, 1, 5, 4], 2))
