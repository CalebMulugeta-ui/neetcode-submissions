import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) < 2:
            return stones[0]
        
        while len(stones) > 1:
            heapq._heapify_max(stones)
            x = heapq._heappop_max(stones)
            y = heapq._heappop_max(stones)
            if x > y:
                stones.append(x-y)
            elif y < x:
                stones.append(y-x)
            else:
                continue
        
        if len(stones)>0:
            return stones[0]
        else:
            return 0



        

        