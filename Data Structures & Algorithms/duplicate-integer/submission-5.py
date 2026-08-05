class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        flag = False
        for e in range(len(nums)):
            for i in range(len(nums)):
                if e == i:
                    continue
                else:
                    if nums[e] == nums[i]:
                        flag = True
        return flag