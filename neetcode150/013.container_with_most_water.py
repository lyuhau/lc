from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        bot = 0
        top = len(heights) - 1
        max_water = 0

        curr_water = min((heights[bot], heights[top])) * (top - bot)
        max_water = max(max_water, curr_water)

        while bot != top:
            if heights[bot] < heights[top]:
                bot += 1
            else:
                top -= 1
            curr_water = min((heights[bot], heights[top])) * (top - bot)
            max_water = max(max_water, curr_water)

        print(max_water)
        return max_water


if __name__ == '__main__':
    solution = Solution()
    solution.maxArea([1,7,2,5,4,7,3,6])
    solution.maxArea([2, 2, 2])
    solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
    solution.maxArea([1, 1])
    solution.maxArea([4, 3, 2, 1, 4])
    solution.maxArea([1, 2, 1])
    solution.maxArea([1, 2, 4, 3])
    solution.maxArea([1, 2, 4, 3, 1, 2, 4, 3])
    solution.maxArea([1, 2, 4, 3, 1, 2, 4, 3, 1, 2, 4, 3])
    solution.maxArea([1, 2, 4, 3, 1, 2, 4, 3, 1, 2, 4, 3, 1, 2, 4, 3])
