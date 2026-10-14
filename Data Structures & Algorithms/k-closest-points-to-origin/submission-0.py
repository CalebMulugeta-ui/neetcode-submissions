import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        myMap = {}
        #key = disctace value = cord
        for i in points:
            cord = (i[0] , i[1])
            myMap[(-math.sqrt( (i[0]**2) + (i[1]**2)), cord) ] = i
        
        myHeap = []

        #iterate thru map, and create a min heap by the values, start doing replacments when length of the heap > k

        """
        -3 [cord]
       -2[cord] -1[cord]

        """
        #key is a tuple hsh = {(distance, (cord)):[cord]}
        for i in myMap.keys():
            if len(myHeap) < k:
                heapq.heappush(myHeap, i)
            else:
                heapq.heappushpop(myHeap, i)

        res = []
        for i in myHeap:
            res.append(myMap[i])

        return res
        