class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r =1
        p = 0 
        while r < len(prices):
            currP = prices[r] - prices[l]
            if currP > p:
                p = currP
            if prices[l] > prices[r]:
                l = r
                r+=1
            else:
                r+=1
        
        return p






        
            
       