class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end  = len(matrix) - 1

        leftPointer = 0
        rightPointer = len(matrix[0]) - 1

        while start <= end:
            middle = (start + end)//2

            if target < matrix[middle][leftPointer]:
                end = middle - 1
            elif target >= matrix[middle][leftPointer] and target <= matrix[middle][rightPointer]:
                if target in matrix[middle]:
                    return True
                else:
                    return False
            else:
                start = middle + 1

        return False
        