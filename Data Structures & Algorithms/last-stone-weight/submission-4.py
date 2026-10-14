import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) < 2:
            return stones[0]

        maxHeap = []
        for i in stones:
            heapq.heappush(maxHeap, -i)
        

        while len(maxHeap) > 1:
            x = -heapq.heappop(maxHeap)
            y = -heapq.heappop(maxHeap)

            if x>y:
                heapq.heappush(maxHeap,-(x-y))
            elif y<x:
                heapq.heappush(maxHeap,-(y-x))


        if len(maxHeap) > 0:
            return -maxHeap[0]
        else:
            return 0