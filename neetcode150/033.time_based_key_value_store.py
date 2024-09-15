from collections import defaultdict
from typing import List, Tuple


class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        return binary_search(self.map[key], timestamp)


def binary_search(values: List[Tuple[int, str]], target: int) -> str:
    if not values or values[0][0] > target:
        return ""

    i = 0
    j = len(values)
    while i != j:
        check = (i + j) // 2
        if values[check][0] == target:
            return values[check][1]
        elif values[check][0] > target:
            j = check
        else:
            i = check + 1
    return values[i - 1][1]


if __name__ == '__main__':
    solution = TimeMap()
    solution.set("foo", "bar1", 1)
    print(solution.get("foo", 1))
    print(solution.get("foo", 3))
    solution.set("foo", "bar4", 4)
    print(solution.get("foo", 3))
    print(solution.get("foo", 4))
    solution.set("foo", "bar6", 6)
    print(solution.get("foo", 5))
    print(solution.get("foo", 6))
    solution.set("foo", "bar7", 7)
    print(solution.get("foo", 7))
