from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arrivals = [(target - pos) / s for pos, s in sorted(zip(position, speed))]
        fleets = 0
        previous = None
        for arrival in reversed(arrivals):
            if not previous or arrival > previous:
                previous = arrival
                fleets += 1
        return fleets


if __name__ == '__main__':
    solution = Solution()
    print(solution.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
    # print(solution.carFleet(10, [1,4], [3,2]))
    # print(solution.carFleet(10, position = [4,1,0,7], speed = [2,2,1,1]))