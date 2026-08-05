class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for e in range(len(nums)):
                if nums[i] + nums[e] == target and i!=e:
                    return [i,e]
                    




        