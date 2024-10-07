import heapq


class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if num < self.findMedian():
            if len(self.small) > len(self.large):
                heapq.heappush(self.large, -heapq.heappop(self.small))
            heapq.heappush(self.small, -num)
        else:
            if len(self.small) < len(self.large):
                heapq.heappush(self.small, -heapq.heappop(self.large))
            heapq.heappush(self.large, num)

    def findMedian(self) -> float:
        if not self.small and not self.large:
            return 0
        if len(self.small) == len(self.large):
            return (self.large[0] - self.small[0]) / 2
        elif len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return self.large[0]


if __name__ == '__main__':
    s = MedianFinder()
    s.addNum(-1)
    print(s.findMedian())
    s.addNum(-2)
    print(s.findMedian())
    s.addNum(-3)
    print(s.findMedian())
    s.addNum(-4)
    print(s.findMedian())
    s.addNum(-5)
    print(s.findMedian())
