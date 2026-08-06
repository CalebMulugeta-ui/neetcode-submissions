class Solution:
    def isPalindrome(self, s: str) -> bool:
            
        newS = s.lower().replace(" ", "")
        print(newS)
        r = len(newS)
        l = 0
        print (r)
        while r-1 >= l and len(newS) > 1:
            if newS[l].isalnum() and newS[r-1].isalnum():
                if newS[l] == newS[r-1]:
                    r -= 1
                    l += 1
                else:
                    return False
            elif not newS[l].isalnum():
                l+=1
            else:
                r-=1
                
        return True
