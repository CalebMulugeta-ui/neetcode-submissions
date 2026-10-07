class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        mL = 0
        mR = len(matrix) - 1

        while mL <= mR:
            mM = (mR + mL)//2

            l=0
            r=len(matrix[mM]) - 1
            while l <= r:
                m = (r+l)//2
                if matrix[mM][m]<target:
                    l = m+1
                elif matrix[mM][m]>target:
                    r = m-1
                else:
                    return True
                    
            middle = (len(matrix[mM]) - 1)//2
            if matrix[mM][middle] < target:
                mL = mM + 1
            else:
                mR = mM - 1

        return False


     
        