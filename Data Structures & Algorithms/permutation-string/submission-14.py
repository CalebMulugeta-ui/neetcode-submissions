class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Map = {}
        for i in s1:
            if i in s1Map:
                s1Map[i] += 1
            else:
                s1Map[i] = 1
        
        s2Map = {}
        l=0
        r=0
        while r < len(s2):
            if s2[r] not in s1:
                l+=1
                r=l
                s2Map.clear()
            else:
                if s2[r] in s2Map:
                    s2Map[s2[r]] +=1
                else:
                    s2Map[s2[r]] = 1
                

                if s1Map[s2[r]] < s2Map[s2[r]]:
                    l+=1
                    r=l
                    s2Map.clear()
                    continue
                
                if r-l+1 == len(s1):
                    if s1Map == s2Map:
                        return True
                    else:
                        s2Map.clear() 
                        l+=1
                        r=l
                else:
                    r+=1

        return False