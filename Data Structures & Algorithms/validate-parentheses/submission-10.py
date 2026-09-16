class Solution:
    def isValid(self, s: str) -> bool:
        hsh = {']':'[', '}':'{',')':'('}
        stack = []


        
        for i in s:
            if i in hsh.values():
                stack.append(i)
            else:
                if len(stack) > 0:
                    if stack.pop() != hsh[i]:
                        return False                
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False

                
        