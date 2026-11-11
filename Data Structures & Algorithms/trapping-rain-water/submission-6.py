class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
            
        l = 0
        r = len(height)-1
        maxL = height[l]
        maxR=height[r]
        trapped = 0

        while l < r:
            if maxL < maxR:
                l+=1
                if (maxL - height[l]) > 0:
                    trapped += maxL - height[l]

                if maxL < height[l]:
                    maxL = height[l]

            else:
                r-=1
                if (maxR - height[r]) > 0:
                    trapped += maxR - height[r]

                if maxR < height[r]:
                    maxR = height[r]
        
        return trapped
                





        