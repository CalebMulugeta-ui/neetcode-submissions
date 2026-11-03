class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        m = 0
        res = nums[m]
        
        while nums[l] > nums[r]:
            m = r+l//2
            if nums[m] < res:
                res = nums[m]

            if nums[m] >= nums[l]:
                l = m+1
            else:
                r = m-1

        if nums[l] < res:
            return nums[l]
        else:
            return nums[m]


        
            

                




         