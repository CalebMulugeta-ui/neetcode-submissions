import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        largest = 0
        for i in piles:
            if i>largest:
                largest = i
        smallest = largest
        l = 1
        r = largest
        while l <= r:
            m = (r+l)//2
            time = 0
            for pile in piles:
                time+=math.ceil(pile/m)
            
            if time > h:
                l = m + 1
            elif time <= h:
                r = m - 1
                if m <= smallest:
                    smallest = m
        return smallest
                



