class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = []
        currNum = 1
        for i in range(len(nums)):
            if i == 0:
                prefix.append(currNum)
                continue
            else:
                currNum *= nums[i-1]
                prefix.append(currNum)

        suffix = []
        currSuf = 1
        for i in range(len(nums) -1 , -1, -1):
            if i == len(nums) -1:
                suffix.append(currSuf)
                continue
            else:
                currSuf *= nums[i+1]
                suffix.append(currSuf)


        suffix.reverse()

        res = []
        for i in range(len(prefix)):
            res.append(prefix[i] * suffix[i])

        return res





        


            




        