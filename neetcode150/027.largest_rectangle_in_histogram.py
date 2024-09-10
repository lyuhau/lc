from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest = 0
        increasing = []
        last = 0
        for i, h in enumerate(heights):
            if h > last:
                increasing.append((h, i, i))
            elif h < last:
                while increasing and increasing[-1][0] > h:
                    check_h, check_start, _ = increasing.pop()
                    largest = max(largest, check_h * (i - check_start))
                if increasing:
                    increasing.append((h, increasing[-1][2]+1, i))
                else:
                    increasing.append((h, 0, i))
            last = h
        while increasing:
            check_h, check_start, _ = increasing.pop()
            largest = max(largest, check_h * (len(heights) - check_start))

        return largest


if __name__ == '__main__':
    solution = Solution()
    print(solution.largestRectangleArea([2, 1, 5, 6, 2, 3]))
    # print(solution.largestRectangleArea([7,1,7,2,2,4]))
    # print(solution.largestRectangleArea([1,3,7]))
