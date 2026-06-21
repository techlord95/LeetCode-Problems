from collections import List 
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS , COLS = len(matrix) , len(matrix[0]) # gets the no of rows and cols 
        
        # pretending matrix to be 1D array 
        left , right = 0 , (ROWS * COLS) - 1 
        while left <=right:
            mid =  left + (right - left) // 2
            #converting 1 D index into 2D Position 
            row , col = mid //COLS , mid%COLS 
            
            if target > matrix[row][col]:
                left = mid + 1 
            elif target < matrix[row][col]:
                right = mid - 1 
            else :
                return True 
        return False 
       
# Time Complexity -> O(log(ROWS * COLS))
# Space Complexity -> O(1)