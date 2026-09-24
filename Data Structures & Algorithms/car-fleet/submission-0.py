class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        hsh = {}
        for i in range(len(position)):
            hsh[position[i]] = i  
        position.sort(reverse=True)
        stack = []
        for i in range(len(position)):
            time = (target - position[i])/speed[hsh[position[i]]]

            if len(stack)==0:
                stack.append(time)
                continue

            if stack[-1] < time:
                stack.append(time)

        return len(stack)

