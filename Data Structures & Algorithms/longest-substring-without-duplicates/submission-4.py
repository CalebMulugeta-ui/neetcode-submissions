class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        r = 0
        sub = 0
        myset = set()
        while r < len(s):
            if s[r] not in myset:
                myset.add(s[r])
                r+=1
            else:
                if len(myset)>sub:
                    sub = len(myset)
                myset.remove(s[l])
                l+=1
                
        
        if len(myset) > sub:
            sub = len(myset)
        
        return sub

        