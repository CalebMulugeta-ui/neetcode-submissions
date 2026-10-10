class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set()
        for i in nums:
            mySet.add(i)

        res = 0

        for i in nums:
            seq = 1
            if i-1 not in mySet:
                counter = 1
                while i+counter in mySet:
                    seq+=1
                    counter += 1
                if seq > res:
                    res = seq


        return res
        