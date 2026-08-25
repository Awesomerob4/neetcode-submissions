import heapq

class MedianFinder:

    def __init__(self):
        self.big = [] #for top half of nums
        self.small = [] # for bottom half, store negatives
        self.smallSize = 0
        self.bigSize = 0
        self.curMedian = 0
        self.heapSize = 0


    def addNum(self, num: int) -> None:
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.big, num)

        # rebalance so sizes differ by at most 1
        if len(self.small) > len(self.big) + 1:
            heapq.heappush(self.big, -heapq.heappop(self.small))
        elif len(self.big) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.big))

    def findMedian(self) -> float:
        if len(self.small) > len(self.big):
            return -self.small[0]
        return (-self.small[0] + self.big[0]) / 2
            