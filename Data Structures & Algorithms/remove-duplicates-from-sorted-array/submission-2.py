class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        leftP = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                nums[leftP] = nums[i]
                leftP += 1
                

        return leftP