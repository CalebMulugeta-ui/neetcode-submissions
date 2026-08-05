# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.quickSortAlgo(pairs, 0, len(pairs)-1)

    def quickSortAlgo(self, arr: List[Pair], start: int, end:int) -> List[Pair]:
        if end - start + 1 <=1:
            return arr

        pivot = arr[end].key
        leftP = start

        for i in range(start,end):
            if arr[i].key < pivot:
                arr[i], arr[leftP] = arr[leftP],arr[i]
                leftP+=1           
        
        arr[leftP], arr[end] = arr[end], arr[leftP]
        
        self.quickSortAlgo(arr, start, leftP-1)
        self.quickSortAlgo(arr, leftP+1, end)

        return arr    