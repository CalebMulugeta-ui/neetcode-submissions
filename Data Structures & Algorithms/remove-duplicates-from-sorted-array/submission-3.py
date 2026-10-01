class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = 1
        while r < len(nums):
            if nums[r] == nums[l]:
                nums.pop(r)
            else:
                l=r
                r+=1
                
        return len(nums)