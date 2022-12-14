import heapq
class MedianFinder:
    def __init__(self):
        self.smallHeap = [] # max heap
        self.largeHeap = [] # min heap

    # Time O(logN)  
    def addNum(self, num: int) -> None:
        # by default when even we get a number we will add it to small heap.
        heapq.heappush(self.smallHeap,(num * -1))

        # see if not smallHeap <= largeHeap is true
        if self.smallHeap and self.largeHeap and ((self.smallHeap[0] * -1) > self.largeHeap[0]):
            val =(heapq.heappop(self.smallHeap) * -1)
            heapq.heappush(self.largeHeap,val)

        # see if its statisty the length condition
        if len(self.smallHeap) > (len(self.largeHeap) + 1):
            val =(heapq.heappop(self.smallHeap) * -1)
            heapq.heappush(self.largeHeap,val)

        if len(self.largeHeap) > (len(self.smallHeap) + 1):
            val = heapq.heappop(self.largeHeap)
            heapq.heappush(self.smallHeap,(val * -1))
     
    # Time O(1) | Space O(1) 
    def findMedian(self) -> float:
        # if any heap length is odd
        if len(self.smallHeap) > len(self.largeHeap):
            return (self.smallHeap[0] * -1)

        if len(self.largeHeap) > len(self.smallHeap):
            return self.largeHeap[0]   

        # in case of even
        return (((self.smallHeap[0] * -1)+self.largeHeap[0]) / 2)    
         
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
