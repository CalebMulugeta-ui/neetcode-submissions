class Solution:
    def isValid(self, s: str) -> bool:
            
        sstack = []
        co = {']':'[','}':'{',')':'('}
        
        for i in s:
            if i in co:
                if sstack and sstack[-1] == co[i]:
                    sstack.pop()
                else:
                    return False
            else:
                sstack.append(i)

        if not sstack:
            return True
        else:
            return False
