class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxLeft = [0]*n
        maxRight = [0]*n
        minLR = [0]*n

        maxLeft[0] = height[0]
        for i in range(1,n):
            maxLeft[i] = max(maxLeft[i-1], height[i-1])

        maxRight[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            maxRight[i] = max(maxRight[i+1], height[i+1])

        for i in range(n):
            minLR[i] = min(maxLeft[i], maxRight[i])    

        final = 0
        for i in range(n):
            trap = minLR[i] - height[i]
            if trap > 0:
                final+=trap
        return final






        