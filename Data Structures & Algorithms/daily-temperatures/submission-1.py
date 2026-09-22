class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        result = []
        for i in temp:
            result.append(i)
        stack = []

        for i in range(len(temp)):
            while stack and temp[i] > temp[stack[-1]]:
                result[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)

        for i in stack:
            result[i] = 0
        
        return result

        

        
