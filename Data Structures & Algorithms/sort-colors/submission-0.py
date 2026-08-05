class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        count = [0,0,0] #[2,2,2]
        for i in nums:
            count[i] += 1

        i=0
        for n in range(len(count)):
            for e in range(count[n]):
                nums[i] = n
                i+=1

        return nums
        