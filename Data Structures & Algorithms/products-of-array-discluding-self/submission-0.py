class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        #prefix
        prefix = []
        for i in range(len(nums)):
            if i == 0:
                prefix.append(1)
                continue
            prefix.append(nums[i-1]*prefix[i-1])
        print(prefix)
        #suffix
        suffix = [0]*len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                suffix[i]= 1
                continue
            suffix[i]= nums[i+1]*suffix[i+1]
        print(suffix)
        result = []
        for i in range(len(prefix)):
            result.append(prefix[i] * suffix[i])
        
        return result
