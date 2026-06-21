class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        
        left_ptr , right_ptr = 0 , len(numbers) -1 
        
        while left_ptr < right_ptr: # non decreasing is increasing order left will always be small than right
            Current_sum = numbers[left_ptr] + numbers[right_ptr] # adding numbers at each pointer 

            if Current_sum > target: # if the sum is > target move rigth_ptr to left 
                right_ptr -= 1
            elif Current_sum < target: 
                left_ptr +=1 
            else:
                return [left_ptr+1 , right_ptr+1] # here current sum == target , here it expects 1 based indexing array starts from 1 not 0 
#         return[] # this is not required , a failsafe if loop fails 
    
    
# Time = O(n)
# Space = O(1)


        
        