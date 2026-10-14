import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        arr = nums[:k]
        heapq.heapify(arr)
        self.k = k

        for i in nums[k:]:
            heapq.heappushpop(arr, i)

        self.heapList = arr
    
    def add(self, val: int) -> int:
        if len(self.heapList) < self.k:
            heapq.heappush(self.heapList, val)
        else:
            heapq.heappushpop(self.heapList, val)

        print(self.heapList)
        return self.heapList[0]







        
