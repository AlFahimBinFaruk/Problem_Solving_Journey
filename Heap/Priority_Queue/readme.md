### Microsoft Interview Question.
* [Question](https://leetcode.com/problems/find-median-from-data-stream/)
* [Neetcode](https://www.youtube.com/watch?v=itmhHWaHupI)

### 
* we gonna use
  * small heap as maxHeap
  * large heap as minHeap
* In python heaps are default MinHeap so to make them MaxHeap we have to multiply them by -1.  
* by default we will push every element to small heap then we will arrange them on these conditons:  
    * smallHeap(maxHeap) <= largeHeap(minHeap)  -> the element value inside each heap