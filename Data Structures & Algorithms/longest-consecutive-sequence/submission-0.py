class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set()
        myhsh = {}
        for i in nums:
            mySet.add(i)
        
        seq = 0
        count = 0
        curr = 0
        for i in nums:
            if i-1 not in mySet:
                curr = i
                while curr in mySet:
                    count += 1
                    curr += 1
                if count > seq:
                    seq = count
                count = 0
        
        return seq
       
        
                

        



        
        