class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        windowSet = set()
        L = 0
        
        for R in range(len(nums)):
            if abs(R-L) > k:
                windowSet.remove(nums[L])
                L+=1
            
            if nums[R] in windowSet:
                return True
            
            windowSet.add(nums[R])
        
        return False



