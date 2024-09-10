from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        forward_rain = []
        last = 0
        for h in height:
            last = max((last, h))
            forward_rain.append(last - h)

        print(forward_rain)

        total = 0
        last = 0
        for h, forward in reversed(list(zip(height, forward_rain))):
            last = max((last, h))
            total += min((last - h, forward))

        return total


if __name__ == '__main__':
    solution = Solution()
    print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
    print(solution.trap([0,2,0,3,1,0,1,3,2,1]))
