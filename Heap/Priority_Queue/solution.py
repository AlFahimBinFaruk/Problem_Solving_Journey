import heapq


class MedianFinder:

    def __init__(self):
        self.smallHeap = []  # MaxHeap
        self.largeHeap = []  # MinHeap
    
    # Time O(logN) | Space O(N)
    def addNum(self, num: int) -> None:
        heapq.heappush(self.smallHeap, -1 * num)

        # make sure than elements of smallHeap are <= largeHeap
        if self.smallHeap and self.largeHeap and (-1 * self.smallHeap[0] > self.largeHeap[0]):
            val = -1 * heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap, val)

        # if uneven?
        if len(self.smallHeap) > len(self.largeHeap) + 1:
            val = -1 * heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap, val)
        if len(self.largeHeap) > len(self.smallHeap) + 1:
            val = heapq.heappop(self.largeHeap)
            heapq.heappush(self.smallHeap, -1 * val)


    # Time O(1) | Space O(1)
    def findMedian(self) -> float:
        # if odd
        if len(self.smallHeap) > len(self.largeHeap):
            return (-1 * self.smallHeap[0])
        if len(self.largeHeap) > len(self.smallHeap):
            return self.largeHeap[0]

        # if even
        return ((-1 * self.smallHeap[0]) + self.largeHeap[0])/2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
