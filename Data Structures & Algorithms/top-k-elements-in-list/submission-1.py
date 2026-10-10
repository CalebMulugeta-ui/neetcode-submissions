class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myMap = {}
        for i in nums:
            if i in myMap:
                myMap[i]+=1
            else:
                myMap[i] = 1

        freq = [[] for i in range(len(nums)+1)]


        for key, value in myMap.items():
            
            freq[value].append(key)
        
        res = []			
        for i in range(len(freq)-1,-1,-1):
            for j in range(len(freq[i])):
                res.append(freq[i][j])
                if len(res) == k:
                    break 
            if len(res) == k:
                break
					
        return res
        