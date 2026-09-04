class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        r = 0
        res = 0
        myhsh = {}
        for r in range(len(s)):
            if s[r] not in myhsh:
                myhsh[s[r]] = 1
            else:
                myhsh[s[r]] += 1
            
            if (r-l + 1) - max(myhsh.values()) > k:
                myhsh[s[l]] -=1
                l += 1



            res = max(res, r-l + 1)

        return res



