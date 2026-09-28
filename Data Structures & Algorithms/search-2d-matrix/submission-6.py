class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        left =0
        right = len(matrix) - 1
        mid = right // 2

        while left <= right:
            if mid == len(matrix) - 1 or (matrix[mid][0] < target and matrix[mid + 1][0] > target):
                break 
            if matrix[mid][0] == target:
                return True     
            mid = (left + right)//2
            if matrix[mid][0] < target :
                left = mid + 1
            elif matrix[mid][0] > target:
                right = mid - 1

        left = 0
        right = len(matrix[mid]) - 1     
        while left <= right:
            middle = (left + right) // 2 
            if matrix[mid][middle] < target :
                left = middle + 1 
            elif matrix[mid][middle] > target:
                right = middle -1 
            elif matrix[mid][middle] == target:
                return True
        return False             



        