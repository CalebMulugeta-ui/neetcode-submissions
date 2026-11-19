class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1P = 0
        n2P = 0
        sortedArr = []
        while n1P < len(nums1) and n2P < len(nums2):
            if nums1[n1P] < nums2[n2P]:
                sortedArr.append(nums1[n1P])
                n1P+=1
            else:
                sortedArr.append(nums2[n2P])
                n2P+=1
        
        if n1P != len(nums1):
            for i in range(n1P, len(nums1)):
                sortedArr.append(nums1[i])

        if n2P != len(nums2):
            for i in range(n2P, len(nums2)):
                sortedArr.append(nums2[i])
        
        mid = len(sortedArr)//2
        if len(sortedArr)%2 == 0:
            return ((sortedArr[mid]+sortedArr[mid-1])/2)
        else:
            return sortedArr[mid]
            
