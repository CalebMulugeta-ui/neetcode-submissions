class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] #(index, hieght)

        stack.append((0,heights[0]))
        for i in range(1, len(heights)):
            currPair = [i,heights[i]]
            while len(stack) > 0 and stack[-1][1] >= heights[i]:
                pair = stack.pop()
                area = pair[1] * (i-pair[0])
                if area > maxArea:
                    maxArea = area
                currPair[0] = pair[0]   
            stack.append(currPair)

        for pair in stack:
            area = (len(heights) - pair[0]) * pair[1]
            if area > maxArea:
                maxArea = area
        
        return maxArea







             