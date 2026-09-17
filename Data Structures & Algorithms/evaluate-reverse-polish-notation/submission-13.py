class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        mySet = {'+','-','*','/'}
        stack = []

        for curr in tokens:
            if curr in mySet:
                if curr == '+':
                    first = stack.pop()
                    second = stack.pop()
                    stack.append(int(first) + int(second))
                elif curr == '-':
                    first = stack.pop()
                    second = stack.pop()
                    stack.append(int(second) - int(first))
                elif curr == '*':
                    first = stack.pop()
                    second = stack.pop()
                    stack.append(int(first) * int(second))
                elif curr == '/':
                    first = stack.pop()
                    second = stack.pop()
                    if first==0 or second == 0:
                        stack.append(0)
                    else:
                        stack.append(int(int(second) / int(first)))
            else:
                stack.append(int(curr))
        
        return stack.pop()



