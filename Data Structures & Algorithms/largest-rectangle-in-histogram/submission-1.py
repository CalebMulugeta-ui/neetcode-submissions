class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        n = 0
        for i in heights:
            if i>n:
                n=i
        
        largestArea = 0
        area = 0
        for i in range(1,n+1):
            currArea = 0
            for j in range(len(heights)):
                if i <= heights[j]:
                    currArea += i 
                else:
                    if currArea > area:
                        area = currArea
                    currArea = 0
            if currArea > area:
                area = currArea
            if area > largestArea:
                largestArea = area
            area = 0
        
        return largestArea







            